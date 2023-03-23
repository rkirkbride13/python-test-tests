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
        receipt = Receipt()
        receipt.add_order(order)
        self.assertEqual(receipt.print_receipt(), "Tea                     1 x 3.65\n")

    def test_multi_item_order_prints(self):
        order = Mock()
        order.list_items.return_value = [['Tea', 1, 3.65], ['Cortado', 1, 4.55]]
        receipt = Receipt()
        receipt.add_order(order)
        self.assertEqual(receipt.print_receipt(), "Tea                     1 x 3.65\nCortado                 1 x 4.55\n")


if __name__ == '__main__':
    unittest.main()