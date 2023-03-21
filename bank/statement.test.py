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

    def test_prints_after_single_withdrawal(self):
        transaction1 = Mock()
        transaction1.format_date.return_value = "01/01/2023"
        transaction1.format_amount.return_value = "10.00 ||"
        transaction2 = Mock()
        transaction2.format_date.return_value = "01/01/2023"
        transaction2.format_amount.return_value = "|| 1.00"
        account = Mock(get_transactions=lambda: [transaction1, transaction2], balance_at=lambda i: 10 if i == 0 else 9)
        statement = Statement(account)
        expected_output = "date || credit || debit || balance\n01/01/2023 || || 1.00 || 9.00\n01/01/2023 || 10.00 || || 10.00"
        self.assertEqual(statement.print_statement(), expected_output)

if __name__ == '__main__':
    unittest.main()