import unittest
from receipt import Receipt
from unittest.mock import Mock

class TestReceipt(unittest.TestCase):
    
    def test_init(self):
        receipt = Receipt()
        self.assertEqual(isinstance(receipt, Receipt), True)
        self.assertEqual(receipt.receipt, [])

    def test_single_item_order_prints(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65]]
        order.calc_tax.return_value = 0.30
        order.calc_bill.return_value = 3.95
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     1 x 3.65\n", receipt.print_receipt(8.5))

    def test_varied_items_order_prints(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        order.calc_tax.return_value = 0.70
        order.calc_bill.return_value = 8.90
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     1 x 3.65\nCortado                 1 x 4.55\n", receipt.print_receipt(8.5))

    def test_multi_item_order_prints(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 2, 3.65]]
        order.calc_tax.return_value = 0.60
        order.calc_bill.return_value = 7.90
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     2 x 3.65\n", receipt.print_receipt(8.5))

    def test_tax_prints(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65]]
        order.calc_tax.return_value = 0.30
        order.calc_bill.return_value = 3.95
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tax                     $0.30\n", receipt.print_receipt(8.5))

    def test_item_total_prints(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        order.calc_tax.return_value = 0.70
        order.calc_bill.return_value = 8.90
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Total                   $8.90\n", receipt.print_receipt(8.5))

    def test_name_and_date_print(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        order.calc_tax.return_value = 0.70
        order.calc_bill.return_value = 8.90
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Robbie\n", receipt.print_receipt(8.5))
        self.assertIn("22/03/2023 10:36:01\n", receipt.print_receipt(8.5))

    def test_full_printed_receipt(self):
        order = Mock()
        order.get_name.return_value = "Robbie"
        order.get_date.return_value = "22/03/2023 10:36:01"
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        order.calc_tax.return_value = 0.70
        order.calc_bill.return_value = 8.90
        receipt = Receipt()
        receipt.add_order(order)
        self.assertEqual(receipt.print_receipt(8.5), "22/03/2023 10:36:01\nRobbie\nTea                     1 x 3.65\nCortado                 1 x 4.55\nTax                     $0.70\nTotal                   $8.90\n")

if __name__ == '__main__':
    unittest.main()