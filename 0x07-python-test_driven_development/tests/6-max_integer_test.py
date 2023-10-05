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
    
    def test_numbers_character(self):
        """Test for a list of numbers and character/s"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 's'])
        with self.assertRaises(TypeError):
            max_integer([-1, -2, -3, 's'])
        with self.assertRaises(TypeError):
            max_integer([1.1, 2.2, 3.3, 's'])
        with self.assertRaises(TypeError):
            max_integer([-1.1, 2.2, -3.3, 's'])

    def test_mixed_characters(self):
        """Test for a mixture of characters in list including +ve and -ve"""
        self.assertEqual(max_integer(['-a', '-d', '-k', '-w']), '-w')
        self.assertEqual(max_integer(['-a', '-d', 'k', '-w']), 'k')
        self.assertEqual(max_integer(['-a', 'z', 'k', '-w']), 'z')

    def test_mixed_list(self):
        """Test for a list containing various types"""
        with self.assertRaises(TypeError):
            max_integer([1, "87", 3, "hot", -3, [78], {87}, '-z', 'a'])

    def test_float_numbers(self):
        """Test for float numbers in a list including +ve and -ve"""
        self.assertEqual(max_integer([9.1, 2.3, 6.8, 0.1]), 9.1)
        self.assertEqual(max_integer([9, 2, 6.8, 0.1]), 9)
        self.assertEqual(max_integer([-9.1, -2.3, 6.8, 0.1]), 6.8)
        self.assertEqual(max_integer([-9, -2, -6.8, -0.1]), -0.1)
        self.assertEqual(max_integer([-9, -2, -6.8, 0.1]), 0.1)


    if __name__ == '__main__':
        unittest.main()
