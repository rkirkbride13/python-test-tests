import unittest
from receipt import Receipt


class TestReceipt(unittest.TestCase):
    
    def test_init(self):
        receipt = Receipt()
        self.assertEqual(isinstance(receipt, Receipt), True)
        self.assertEqual(receipt.receipt, [])

if __name__ == '__main__':
    unittest.main()