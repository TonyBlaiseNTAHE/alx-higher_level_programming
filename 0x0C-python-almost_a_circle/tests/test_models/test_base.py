#!/usr/bin/python3
"""class Test for Base
"""
from models.base import Base
import unittest


class  TestBase(unittest.TestCase):
    """
    test for base method
    """
    def test_0(self):
        """first test"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(34)
        self.assertEqual(b4.id, 34)

        b5 = Base()
        self.assertEqual(b1.id, 1)

        if __name__ == '__main__':
            unittest.main()