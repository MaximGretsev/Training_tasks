import unittest

from binary_search import BinarySearch


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.array = [i for i in range(0, 101)] + [102]
        self.binary = BinarySearch()

    def test_existing(self):
        self.assertEqual(0, self.binary.binary_search(0, self.array))
        self.assertEqual(67, self.binary.binary_search(67, self.array))
        self.assertEqual(89, self.binary.binary_search(89, self.array))

    def test_not_existing(self):
        self.assertNotEqual(103, self.binary.binary_search(103, self.array), msg="Element 103 does not in the seq")
        self.assertNotEqual(-1, self.binary.binary_search(-1, self.array), msg='Element -1 does not in the seq')

    def test_wrong_data_type(self):
        self.assertNotEqual('123', self.binary.binary_search('123', self.array), msg='str does not in Array')