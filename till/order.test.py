import unittest
from order import Order
from unittest.mock import Mock


class TestOrder(unittest.TestCase):
    
    def test_add_name(self):
        order = Order()
        order.set_name("Robbie")
        self.assertEqual(order.get_name(), 'Robbie')

    def test_add_item(self):
        item = Mock()
        item.get_name.return_value = 'Tea'
        item.get_price.return_value = 3.65
        order = Order()
        order.add_item(item)
        self.assertEqual(order.list_items(), [['Tea', 1, 3.65]])

    def test_multiple_different_items_added(self):
        item = Mock()
        item.get_name.return_value = 'Tea'
        item.get_price.return_value = 3.65
        order = Order()
        order.add_item(item)
        item.get_name.return_value = 'Cortado'
        item.get_price.return_value = 4.55
        order.add_item(item)

        self.assertEqual(order.list_items(), [['Tea', 1, 3.65], ['Cortado', 1, 4.55]])

    def test_multiple_same_item_added(self):
        item = Mock()
        item.get_name.return_value = 'Tea'
        item.get_price.return_value = 3.65
        order = Order()
        order.add_item(item)
        order.add_item(item)
        self.assertEqual(order.list_items(), [['Tea', 2, 3.65]])

if __name__ == '__main__':
    unittest.main()