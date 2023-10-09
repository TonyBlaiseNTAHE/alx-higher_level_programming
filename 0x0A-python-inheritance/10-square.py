#!/usr/bin/python3
"""Module that holds the class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
class Square inherits from Rectangle
"""


class Square(Rectangle):
    """
    initializing the square class
    Args: size - the size of the square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """computes an area of a Square
        """
        return self.__size * self.__size
