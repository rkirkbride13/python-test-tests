import unittest
from order import Order


class TestOrder(unittest.TestCase):
    
    def test_add_name(self):
        order = Order()
        order.set_name("Robbie")
        self.assertEqual(order.get_name(), 'Robbie')


if __name__ == '__main__':
    unittest.main()