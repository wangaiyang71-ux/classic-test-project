"""账户流水记录。"""

from decimal import Decimal
from enum import Enum


class TransactionType(str, Enum):
    """资金变动类型。"""

    OPENING = "opening"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class Transaction:
    """一笔不可变的账户流水。"""

    def __init__(
        self,
        transaction_type: TransactionType,
        amount: Decimal,
        balance_after: Decimal,
    ) -> None:
        self._transaction_type = transaction_type
        self._amount = amount
        self._balance_after = balance_after

    @property
    def transaction_type(self) -> TransactionType:
        return self._transaction_type

    @property
    def amount(self) -> Decimal:
        return self._amount

    @property
    def balance_after(self) -> Decimal:
        return self._balance_after
