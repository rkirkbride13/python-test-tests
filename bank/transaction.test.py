import unittest
from datetime import datetime
from unittest.mock import Mock
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_init(self):
        fake_date = Mock()
        transaction = Transaction(1, fake_date)
        self.assertTrue(isinstance(transaction, Transaction))

    def test_deposit(self):
        transaction = Transaction(1, datetime(2023, 1, 23))
        self.assertEqual(transaction.amount, 1)
        self.assertEqual(transaction.format_date(), '23/01/2023')
        self.assertEqual(transaction.format_amount(), '1.00 ||')

    def test_withdrawal(self):
        transaction = Transaction(-1, datetime(2023, 1, 23))
        self.assertEqual(transaction.amount, -1)
        self.assertEqual(transaction.format_date(), '23/01/2023')
        self.assertEqual(transaction.format_amount(), '|| 1.00')

if __name__ == '__main__':
    unittest.main()