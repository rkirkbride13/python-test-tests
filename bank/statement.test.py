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

    def test_prints_after_multiple_deposits(self):
        transaction = Mock()
        transaction.format_date.return_value = "01/01/2023"
        transaction.format_amount.return_value = "5.00 ||"
        account = Mock(get_transactions=lambda: [transaction, transaction, transaction], balance_at=lambda i: 5 if i == 0 else 10 if i == 1 else 15)
        statement = Statement(account)
        expected_output = "date || credit || debit || balance\n01/01/2023 || 5.00 || || 15.00\n01/01/2023 || 5.00 || || 10.00\n01/01/2023 || 5.00 || || 5.00"
        self.assertEqual(statement.print_statement(), expected_output)

    def test_prints_after_multiple_withdrawals(self):
        transaction1 = Mock()
        transaction1.format_date.return_value = "01/01/2023"
        transaction1.format_amount.return_value = "45.00 ||"
        transaction2 = Mock()
        transaction2.format_date.return_value = "01/01/2023"
        transaction2.format_amount.return_value = "|| 10.00"
        transaction3 = Mock()
        transaction3.format_date.return_value = "01/01/2023"
        transaction3.format_amount.return_value = "|| 25.00"
        account = Mock(get_transactions=lambda: [transaction1, transaction2, transaction3], balance_at=lambda i: 45 if i == 0 else 35 if i == 1 else 10)
        statement = Statement(account)
        expected_output = "date || credit || debit || balance\n01/01/2023 || || 25.00 || 10.00\n01/01/2023 || || 10.00 || 35.00\n01/01/2023 || 45.00 || || 45.00"
        self.assertEqual(statement.print_statement(), expected_output)

    def test_prints_with_example_transactions(self):
        transaction1 = Mock()
        transaction1.format_date.return_value = "10/01/2023"
        transaction1.format_amount.return_value = "1000.00 ||"
        transaction2 = Mock()
        transaction2.format_date.return_value = "13/01/2023"
        transaction2.format_amount.return_value = "2000.00 ||"
        transaction3 = Mock()
        transaction3.format_date.return_value = "14/01/2023"
        transaction3.format_amount.return_value = "|| 500.00"
        account = Mock(get_transactions=lambda: [transaction1, transaction2, transaction3], balance_at=lambda i: 1000 if i == 0 else 3000 if i == 1 else 2500)
        statement = Statement(account)
        expected_output = "date || credit || debit || balance\n14/01/2023 || || 500.00 || 2500.00\n13/01/2023 || 2000.00 || || 3000.00\n10/01/2023 || 1000.00 || || 1000.00"
        self.assertEqual(statement.print_statement(), expected_output)

if __name__ == '__main__':
    unittest.main()