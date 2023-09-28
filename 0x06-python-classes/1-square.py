#!/usr/bin/python3
""" Represents a Square.
    This class defines a square and its properties
"""


class Square:
    """Initialize a square instance with a given side length.
    Args:
        value (int, optional): The side length of the square. Defaults to 0.
    """
    def __init__(self, size=0):
        """ initializes __size of self with size """
        self.__size = size
