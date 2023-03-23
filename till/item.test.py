import unittest
from item import Item

class TestItem(unittest.TestCase):
    def test_init(self):
        item = Item()
        item.set_name('Tea')
        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.get_name(), 'Tea')
        self.assertEqual(item.get_price(),3.65)

if __name__ == '__main__':
    unittest.main()