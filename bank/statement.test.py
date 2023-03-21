import unittest
from unittest.mock import Mock
from statement import Statement

class TestStatement(unittest.TestCase):
    def test_prints_after_single_deposit(self):
        transaction = Mock()
        transaction.format_date.return_value = "01/01/2023"
        transaction.format_amount.return_value = "1.00 ||"
        account = Mock()
        account.get_transactions.return_value = [transaction]
        account.balance_at.return_value = 1
        statement = Statement(account)
        expected_output = "date || credit || debit || balance\n01/01/2023 || 1.00 || || 1.00"
        self.assertEqual(statement.print_statement(), expected_output)

if __name__ == '__main__':
    unittest.main()