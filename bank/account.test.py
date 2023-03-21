import unittest
from unittest.mock import Mock
from account import Account
from unittest.mock import MagicMock


class TestAccount(unittest.TestCase):
    def test_balance_of_zero_initially(self):
        account = Account()
        self.assertTrue(isinstance(account, Account))

    def test_deposit_balance(self):
        account = Account()
        transaction = Mock(amount=1, date='01/01/2023')
        account.add_transaction(transaction)
        self.assertEqual(account.latest_balance(), 1.00)


if __name__ == '__main__':
    unittest.main()