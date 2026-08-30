"""银行转账领域异常。"""


class BankError(Exception):
    """银行业务异常基类。"""


class InvalidAmountError(BankError):
    """金额不合法。"""


class InsufficientFundsError(BankError):
    """余额不足。"""


class SameAccountError(BankError):
    """转出账户与转入账户相同。"""
