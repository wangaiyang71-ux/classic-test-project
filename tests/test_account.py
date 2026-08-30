"""BankAccount 单元测试。"""

import unittest
from decimal import Decimal

from classic_bank.account import BankAccount
from classic_bank.exceptions import InsufficientFundsError, InvalidAmountError


class BankAccountTest(unittest.TestCase):
    def test_open_account_with_zero_balance(self) -> None:
        account = BankAccount("A001", "张三", Decimal("0.00"))
        self.assertEqual(account.balance, Decimal("0.00"))

    def test_deposit_increases_balance(self) -> None:
        account = BankAccount("A001", "张三", Decimal("10.00"))
        account.deposit(Decimal("2.50"))
        self.assertEqual(account.balance, Decimal("12.50"))

    def test_withdraw_decreases_balance(self) -> None:
        account = BankAccount("A001", "张三", Decimal("10.00"))
        account.withdraw(Decimal("3.00"))
        self.assertEqual(account.balance, Decimal("7.00"))

    def test_withdraw_over_balance_fails(self) -> None:
        account = BankAccount("A001", "张三", Decimal("1.00"))
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(Decimal("1.01"))
        self.assertEqual(account.balance, Decimal("1.00"))

    def test_reject_non_positive_deposit(self) -> None:
        account = BankAccount("A001", "张三", Decimal("1.00"))
        with self.assertRaises(InvalidAmountError):
            account.deposit(Decimal("0.00"))


if __name__ == "__main__":
    unittest.main()
