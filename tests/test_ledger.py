"""账户流水与转账限额测试。"""

import unittest
from decimal import Decimal

from classic_bank.account import BankAccount
from classic_bank.constants import MAX_SINGLE_TRANSFER
from classic_bank.exceptions import TransferLimitExceededError
from classic_bank.transaction import TransactionType
from classic_bank.transfer_service import TransferService


class LedgerTest(unittest.TestCase):
    def test_opening_and_deposit_are_recorded(self) -> None:
        account = BankAccount("A001", "张三", Decimal("10.00"))
        account.deposit(Decimal("2.00"))
        types = [item.transaction_type for item in account.ledger]
        self.assertEqual(types, [TransactionType.OPENING, TransactionType.DEPOSIT])
        self.assertEqual(account.ledger[-1].balance_after, Decimal("12.00"))


class TransferLimitTest(unittest.TestCase):
    def test_reject_amount_over_single_limit(self) -> None:
        source = BankAccount("A001", "张三", MAX_SINGLE_TRANSFER + Decimal("1.00"))
        target = BankAccount("A002", "李四", Decimal("0.00"))
        service = TransferService()
        with self.assertRaises(TransferLimitExceededError):
            service.transfer(source, target, MAX_SINGLE_TRANSFER + Decimal("0.01"))
        self.assertEqual(source.balance, MAX_SINGLE_TRANSFER + Decimal("1.00"))
        self.assertEqual(target.balance, Decimal("0.00"))


if __name__ == "__main__":
    unittest.main()
