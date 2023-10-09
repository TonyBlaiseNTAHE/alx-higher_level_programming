#!/usr/bin/python3
"""
BaseGeometry class

"""

class BaseGeometry:
    """area method"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validator method

        args: name - the name
              value - the value
        raise error if value is not int
        raise errror if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""
Rectangle class inherit from BaseGeometry
"""

class Rectangle(BaseGeometry):
    """constructor"""
    def __init__(self, size):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", height)
        self.integer_validator("heigh", width)
    def __str__(self):
        """returns"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
    def area(self):
        """Returns the area of a Rectangle"""
        return self.__width * self.__height

class Square(Rectangle):
    """A square - child of Rectangle
    """
    def __init__(self, size):
        """Initializes a new square

        Args:
            size (int): length of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of square
        """
        return super().area()