"""账户之间的转账服务。"""

from decimal import Decimal

from classic_bank.account import BankAccount
from classic_bank.constants import CURRENCY_CODE, MIN_TRANSFER_AMOUNT
from classic_bank.exceptions import InvalidAmountError, SameAccountError
from classic_bank.logger import get_logger

logger = get_logger()


class TransferService:
    """在两个账户之间完成一笔转账。"""

    def transfer(self, source: BankAccount, target: BankAccount, amount: Decimal) -> None:
        """从 source 转到 target。先校验，再扣款，再入账。"""
        if source is None or target is None:
            raise ValueError("转出账户和转入账户都不能为空")
        if source.account_id == target.account_id:
            logger.warning("拒绝同账户转账 account_id=%s", source.account_id)
            raise SameAccountError("不能向同一账户转账")
        if amount < MIN_TRANSFER_AMOUNT:
            raise InvalidAmountError("转账金额低于最低限额")

        logger.info(
            "开始转账 from=%s to=%s amount=%s %s",
            source.account_id,
            target.account_id,
            amount,
            CURRENCY_CODE,
        )
        source.withdraw(amount)
        try:
            target.deposit(amount)
        except Exception:
            logger.exception("转入失败，开始回滚 from=%s to=%s amount=%s", source.account_id, target.account_id, amount)
            source.deposit(amount)
            raise
        logger.info(
            "转账完成 from=%s to=%s amount=%s source_balance=%s target_balance=%s",
            source.account_id,
            target.account_id,
            amount,
            source.balance,
            target.balance,
        )
