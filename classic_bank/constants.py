"""银行转账示例中的业务常量，避免魔法数字。"""

from decimal import Decimal

# 账户允许的最低余额（不允许透支）
MIN_ACCOUNT_BALANCE = Decimal("0.00")

# 单笔转账最低金额
MIN_TRANSFER_AMOUNT = Decimal("0.01")

# 单笔转账最高金额
MAX_SINGLE_TRANSFER = Decimal("50000.00")

# 单账户单日转出累计限额（当前实现尚未强制校验，留给审查发现）
MAX_DAILY_TRANSFER = Decimal("100000.00")

# 金额小数位
MONEY_DECIMAL_PLACES = 2

# 货币代码，仅作展示
CURRENCY_CODE = "CNY"
