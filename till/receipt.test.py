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
        order.list_items.return_value = [['Tea', 1, 3.65]]
        order.item_total.return_value = 3.65
        order.calc_tax.return_value = 0.30
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     1 x 3.65\n", receipt.print_receipt())

    def test_varied_items_order_prints(self):
        order = Mock()
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        order.item_total.return_value = 8.20
        order.calc_tax.return_value = 0.70
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     1 x 3.65\nCortado                 1 x 4.55\n", receipt.print_receipt())

    def test_multi_item_order_prints(self):
        order = Mock()
        order.list_items.return_value = [['Tea', 2, 3.65]]
        order.item_total.return_value = 7.30
        order.calc_tax.return_value = 0.60
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     2 x 3.65\n", receipt.print_receipt())

    def test_tax_prints(self):
        order = Mock()
        order.list_items.return_value = [['Tea', 1, 3.65]]
        order.item_total.return_value = 3.65
        order.calc_tax.return_value = 0.30
        receipt = Receipt()
        receipt.add_order(order)
        self.assertIn("Tea                     1 x 3.65\nTax                     $0.30\n", receipt.print_receipt())

if __name__ == '__main__':
    unittest.main()