#!/usr/bin/python3
"""module that holds class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

"""
class that inherits from Rectangle
"""


class Square(Rectangle):
    """initialising the constructor"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Rectangle represenation
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
