#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """testing is the both side are equals"""
        self.assertAlmostEqual(max_integer([1,2,3,4]), 4)
        self.assertAlmostEqual(max_integer([1,2,4,5,45]), 45)
        self.assertAlmostEqual(max_integer([14,20,54,65,80]), 80)
        self.assertAlmostEqual(max_integer([0,]), 0)
        self.assertAlmostEqual(max_integer([1,2,]), 2)
        self.assertAlmostEqual(max_integer([100,545,678]), 678)
        self.assertAlmostEqual(max_integer([5.6,3.4,-2,-45]), 5.6)
        self.assertAlmostEqual(max_integer([-1,-2,-4,-4,0]), 0)
    
    def test_type(self):
        """raise error if any incorrect type is passed"""
        self.assertRaises(TypeError, max_integer, 2, 't', 3, 4, 5, 6)
        self.assertRaises(TypeError, max_integer, "tony", 'i', 45, 6, 7 ,8)
        self.assertRaises(TypeError, max_integer, 0, '+', 45, 6, 7 ,8)
        self.assertRaises(TypeError, max_integer, 1, 2, 'i')
        self.assertRaises(TypeError, max_integer, 0, '+', 7 ,8)
    def test_syntax(self):
        with self.assertRaises(SyntaxError):
            eval("max_integer([1,,0])")
            eval("max_integer([hello, 07])")
    def test_name(self):
        with self.assertRaises(NameError):
            eval("max_integer([hello])")
            eval("max_integer([hello, hi])")
            eval("max_integer([a, z])")


    if __name__ == '__main__':
        unittest.main()
