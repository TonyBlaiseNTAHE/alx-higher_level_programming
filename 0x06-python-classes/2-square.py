#!/usr/bin/python3
"""Representing a class square
    This a class representation and its properties"""


class Square:
    """Defining __init__ function"""
    def __init__(self, size=0):
        """check if size is an integer, if yes and instantiate it"""
        if isinstance(size, int):
            """initializes __size of self with size"""
            self.__size = size
        else:
            """ raise an TypeError message """
            raise TypeError("size must be an intger")
        if size < 0:
            """raise an ValueError message """
            raise ValueError("size must be >= 0")
