import unittest

from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO

class TestRectangleArea(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
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
        
    def test_str(self):
        """testing string function"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, 49)  
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2) 
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.area(), 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (49) 3/4 - 1/2")
    def test_toDictionary(self):
        r2 = Rectangle(1, 2, 3, 4)
        output = {'x': 3, 'y': 4, 'id': 50, 'height': 2, 'width': 1}
        self.assertEqual(r2.to_dictionary(), output)
    def test_update(self):
        """testing update function"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (51) 10/10 - 10/10")
        r1.update(1, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 4/10 - 2/3")
        r1.update(20, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (20) 4/10 - 2/3")
        r1.update(1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 4/10 - 2/3")
        r1.update(**{'id':45})
        self.assertEqual(r1.__str__(), "[Rectangle] (45) 4/10 - 2/3")
        r1.update(**{'width': 5, 'height': 6})
        self.assertEqual(r1.__str__(), "[Rectangle] (45) 4/10 - 5/6")
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)


    def test_validator(self):
        pass

if __name__ == '__main__':
    unittest.main()
