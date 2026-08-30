"""TransferService 单元测试。"""

import unittest
from decimal import Decimal

from classic_bank.account import BankAccount
from classic_bank.exceptions import InsufficientFundsError, SameAccountError
from classic_bank.transfer_service import TransferService


class TransferServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.source = BankAccount("A001", "张三", Decimal("100.00"))
        self.target = BankAccount("A002", "李四", Decimal("20.00"))
        self.service = TransferService()

    def test_transfer_moves_money(self) -> None:
        self.service.transfer(self.source, self.target, Decimal("30.00"))
        self.assertEqual(self.source.balance, Decimal("70.00"))
        self.assertEqual(self.target.balance, Decimal("50.00"))

    def test_transfer_fails_when_balance_not_enough(self) -> None:
        with self.assertRaises(InsufficientFundsError):
            self.service.transfer(self.source, self.target, Decimal("100.01"))
        self.assertEqual(self.source.balance, Decimal("100.00"))
        self.assertEqual(self.target.balance, Decimal("20.00"))

    def test_reject_same_account_transfer(self) -> None:
        with self.assertRaises(SameAccountError):
            self.service.transfer(self.source, self.source, Decimal("1.00"))
        self.assertEqual(self.source.balance, Decimal("100.00"))


if __name__ == "__main__":
    unittest.main()
