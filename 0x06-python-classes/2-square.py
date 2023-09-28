#!/usr/bin/python3
"""Representing a class square
    This a class representation and its properties"""


class Square:
    """Defining __init__ function"""
    def __init__(self, size=0):
        """if statement """
        if type(size) != int:
            """ raise Error """
            raise TypeError("size must be an intger")
        elif size < 0:
            """raise Error  """
            raise ValueError("size must be >= 0")
        else:
            """initializes __size of self with size"""
            self.__size = size
