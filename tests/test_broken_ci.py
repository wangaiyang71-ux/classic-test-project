"""故意失败的测试，用于验证 CI 会拦住有问题的提交。"""

import unittest
from decimal import Decimal

from classic_bank.account import BankAccount


class BrokenCiTest(unittest.TestCase):
    def test_balance_must_stay_non_negative(self) -> None:
        account = BankAccount("A001", "张三", Decimal("1.00"))
        # 故意写错期望，让 CI 失败
        self.assertEqual(account.balance, Decimal("999.00"))


if __name__ == "__main__":
    unittest.main()
