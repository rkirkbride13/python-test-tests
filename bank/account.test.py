import unittest
from unittest.mock import Mock
from account import Account
from unittest.mock import MagicMock


class TestAccount(unittest.TestCase):
    def test_balance_of_zero_initially(self):
        account = Account()
        self.assertTrue(isinstance(account, Account))

    def test_positive_balance_on_deposit(self):
        account = Account()
        transaction = Mock(amount=1, date='01/01/2023')
        account.add_transaction(transaction)
        self.assertEqual(account.latest_balance(), 1.00)

    def test_balance_reduced_on_withdrawal(self):
        account = Account()
        transaction1 = Mock(amount=10, date='01/01/2023')
        transaction2 = Mock(amount=-1, date='01/01/2023')
        account.add_transaction(transaction1)
        account.add_transaction(transaction2)
        self.assertEqual(account.latest_balance(), 9.00)

    def test_positive_balance_multiple_deposits(self):
        account = Account()
        transaction1 = Mock(amount=1, date='01/01/2023')
        transaction2 = Mock(amount=2, date='01/01/2023')
        transaction3 = Mock(amount=9, date='01/01/2023')
        account.add_transaction(transaction1)
        account.add_transaction(transaction2)
        account.add_transaction(transaction3)
        self.assertEqual(account.latest_balance(), 12.00)

    def test_balance_multiple_withdrawals(self):
        account = Account()
        transaction1 = Mock(amount=20, date='01/01/2023')
        transaction2 = Mock(amount=-2, date='01/01/2023')
        transaction3 = Mock(amount=-5, date='01/01/2023')
        transaction4 = Mock(amount=-11, date='01/01/2023')
        account.add_transaction(transaction1)
        account.add_transaction(transaction2)
        account.add_transaction(transaction3)
        account.add_transaction(transaction4)
        self.assertEqual(account.latest_balance(), 2.00)


    def test_error_raised_if_insufficient_funds(self):
        account = Account()
        transaction1 = Mock(amount=10, date='01/01/2023')
        transaction2 = Mock(amount=-100, date='01/01/2023')
        account.add_transaction(transaction1)
        with self.assertRaises(Exception):
            account.add_transaction(transaction2)

if __name__ == '__main__':
    unittest.main()