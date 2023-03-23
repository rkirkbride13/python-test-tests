import unittest
from item import Item

class TestItem(unittest.TestCase):
    def test_name_and_price(self):
        item = Item()
        item.set_name('Tea')
        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.get_name(), 'Tea')
        self.assertEqual(item.get_price(),3.65)

    def test_error_raised_if_item_nonexistant(self):
        item = Item()
        with self.assertRaises(Exception):
            item.set_name('Pizza')

if __name__ == '__main__':
    unittest.main()