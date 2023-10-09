#!/usr/bin/python3
"""Class BaseGeometry
"""


class BaseGeometry:
    """defines area method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """if statement"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""
Rectangle class
"""


class Rectangle(BaseGeometry):
    """define constructor"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)
