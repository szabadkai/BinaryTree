import unittest
from BinaryTree import BinaryTree as bt


class TestBinaryTree(unittest.TestCase):
    def test_object_creation(self):
        a = bt(1, 1)
        self.assertEqual(a.key, 1)

    def test_insert(self):
        a = bt(1, 1)
        a.insert(2, 1)
        self.assertEqual(a.right.key, 2)

    def test_insert_has_key(self):
        a = bt(1, 1)
        a.insert(1, 2)
        self.assertEqual(a.data, 2)

    def test_min(self):
        a = bt(1, 1)
        a.insert(2, 1)
        self.assertEqual(a.min, 1)

    def test_min_has_left(self):
        a = bt(1, 1)
        a.insert(0, 1)
        self.assertEqual(a.min, 0)

    def test_getitem(self):
        a = bt(1, "asdf")
        self.assertEqual(a[1], 'asdf')

    def test_1k_inserts(self):
        a = bt(0, 0)
        for i in range(100):
            a.insert(i, i+1)
        self.assertEqual(a[21], 22)

    def test_size(self):
        a = bt(0, 0)
        for i in range(100):
            a.insert(i, i+1)
        self.assertEqual(len(a), 101)
