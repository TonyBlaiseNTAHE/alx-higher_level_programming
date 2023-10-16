"""def add(*args):
    sum = 0
    for i in args:
        sum += i
    print("sum is {:d}".format(sum))


add(1, 3 , 6)
add(1, 34 , 6, 8, 9)
add (2, 4, 5, 89)
def info_person(*args, **kwargs):
    for value in kwargs.values():
        print(f"{value}")
    print(args)

info_person(1, 2, name="Tony", xge=30)"""
a = 2
print("{:d}".format(a)) 




import unittest

from models.rectangle import Rectangle
import sys
from io import StringIO

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        res = Rectangle(3,6)
        self.assertEqual(res.area(), 18)
        res = Rectangle(2,2)
        self.assertEqual(res.area(), 4)
        res = Rectangle(1,6)
        self.assertEqual(res.area(), 6)
        res = Rectangle(5,6)
        self.assertEqual(res.area(), 30)
        res = Rectangle(4,4)
        self.assertEqual(res.area(), 16)
        res = Rectangle(30,2)
        self.assertEqual(res.area(), 60)
        res = Rectangle(1,1)
        self.assertEqual(res.area(), 1)

    def test_area_type(self):
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.height = ()

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.height = 2.3

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.height = 'h'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.height = 'hello'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.height = {}
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.width = ()

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.width = 2.3

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.width = 'h'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.width = 'hello'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.width = {}
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.x = ()

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.x = 2.3

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.x = 'h'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.x = 'hello'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.x = {}
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.y = ()

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.y = 2.3

        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.y = 'h'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.y = 'hello'
        
        res = Rectangle(3,6)
        with self.assertRaises(TypeError):
            res.y = {}
    
    def test_area_Value(self):
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.height = 0
    
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.height = -1

        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.height = -23
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.height = -4
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.height = -2
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.width = 0
    
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.width = -1

        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.width = -23
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.width = -4
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.width = -2
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.x = -4
    
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.x = -10

        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.x = -23
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.x = -4
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.x = -2
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.y = -10
    
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.y = -10

        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.y = -23
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.y = -4
        
        res = Rectangle(3,6)
        with self.assertRaises(ValueError):
            res.y = -2
        
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_display(self):
        rect = Rectangle(3, 3)
        rect.display()
        printed_output = sys.stdout.getvalue()
        expected_output = "###\n###\n###\n"
        self.assertEqual(printed_output, expected_output)

    def test_2(self):
        """test 2"""
        r1 = Rectangle(3, 5, 6, 0)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 6/0 - 3/5")
        self.assertEqual(r1.area(), 15)
    def test_validator(self):
        pass

if __name__ == '__main__':
    unittest.main()