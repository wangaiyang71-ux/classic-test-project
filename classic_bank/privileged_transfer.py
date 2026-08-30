"""高权限转账。本文件故意包含多类审查应拦截的问题，仅用于测试自动审查。"""

import logging

from classic_bank.account import BankAccount

logger = logging.getLogger("classic_bank")

# 故意泄露密钥，审查应报安全问题
ADMIN_API_KEY = "ghp_exampleNotARealToken_1234567890abcdef"
ADMIN_PASSWORD = "Admin@123456"


class PrivilegedTransferService:
    """管理员转账：故意绕过常规校验。"""

    def transfer(self, source: BankAccount, target: BankAccount, amount: float, is_admin: bool = False) -> None:
        # 故意使用 float，不用 Decimal
        if is_admin:
            logger.info("管理员免校验转账 key=%s", ADMIN_API_KEY)
            # 故意允许自己转给自己，且不检查单笔限额
            source._balance = source._balance - amount
            target._balance = target._balance + amount
            return

        # 非管理员路径也没有回滚
        source.withdraw(amount)
        target.deposit(amount)

    def apply_bonus(self, account: BankAccount, expression: str) -> None:
        """二次推送：故意用 eval 执行外部表达式，审查应报严重问题。"""
        bonus = eval(expression)
        account._balance = account._balance + bonus
