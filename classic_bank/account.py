"""银行账户实体。"""

from decimal import Decimal, ROUND_HALF_UP

from classic_bank.constants import CURRENCY_CODE, MIN_ACCOUNT_BALANCE, MONEY_DECIMAL_PLACES
from classic_bank.exceptions import InsufficientFundsError, InvalidAmountError
from classic_bank.logger import get_logger
from classic_bank.transaction import Transaction, TransactionType

logger = get_logger()


class BankAccount:
    """表示一个不可透支的银行账户。"""

    def __init__(self, account_id: str, owner_name: str, opening_balance: Decimal) -> None:
        if not account_id:
            raise ValueError("account_id 不能为空")
        if not owner_name:
            raise ValueError("owner_name 不能为空")

        self._account_id = account_id
        self._owner_name = owner_name
        self._ledger: list[Transaction] = []
        self._balance = self._normalize_amount(
            opening_balance,
            field_name="opening_balance",
            allow_zero=True,
        )
        if self._balance < MIN_ACCOUNT_BALANCE:
            raise InvalidAmountError("开户金额不能低于最低余额")
        self._record(TransactionType.OPENING, self._balance)

        logger.info(
            "创建账户 account_id=%s owner=%s balance=%s %s",
            self._account_id,
            self._owner_name,
            self._balance,
            CURRENCY_CODE,
        )

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @property
    def balance(self) -> Decimal:
        return self._balance

    @property
    def ledger(self) -> tuple[Transaction, ...]:
        """返回只读流水，避免外部直接改内部列表。"""
        return tuple(self._ledger)

    def deposit(self, amount: Decimal) -> None:
        """存入资金。"""
        normalized = self._normalize_amount(amount, field_name="deposit")
        self._balance += normalized
        self._record(TransactionType.DEPOSIT, normalized)
        logger.info("存款成功 account_id=%s amount=%s balance=%s", self._account_id, normalized, self._balance)

    def withdraw(self, amount: Decimal) -> None:
        """取出资金，余额不足时失败。"""
        normalized = self._normalize_amount(amount, field_name="withdraw")
        if self._balance - normalized < MIN_ACCOUNT_BALANCE:
            logger.warning(
                "取款失败，余额不足 account_id=%s amount=%s balance=%s",
                self._account_id,
                normalized,
                self._balance,
            )
            raise InsufficientFundsError("账户余额不足")

        self._balance -= normalized
        self._record(TransactionType.WITHDRAW, normalized)
        logger.info("取款成功 account_id=%s amount=%s balance=%s", self._account_id, normalized, self._balance)

    def _record(self, transaction_type: TransactionType, amount: Decimal) -> None:
        self._ledger.append(
            Transaction(
                transaction_type=transaction_type,
                amount=amount,
                balance_after=self._balance,
            )
        )

    def _normalize_amount(
        self,
        amount: Decimal,
        field_name: str,
        allow_zero: bool = False,
    ) -> Decimal:
        if not isinstance(amount, Decimal):
            raise InvalidAmountError(f"{field_name} 必须是 Decimal")
        if allow_zero:
            if amount < MIN_ACCOUNT_BALANCE:
                raise InvalidAmountError(f"{field_name} 不能为负数")
        elif amount <= MIN_ACCOUNT_BALANCE:
            raise InvalidAmountError(f"{field_name} 必须大于 0")

        quantize_unit = Decimal("1").scaleb(-MONEY_DECIMAL_PLACES)
        return amount.quantize(quantize_unit, rounding=ROUND_HALF_UP)
