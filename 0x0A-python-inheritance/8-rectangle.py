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

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", height)
        self.integer_validator("heigh", width)
