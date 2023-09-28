#!/usr/bin/python3
"""Representing a class square"""


class Square:
    """Defining a function called __init"""
    def __init__(self, size=0):
        """if statement"""
        if not isinstance(size, int):
            """raise Error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raise Error"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """defining function called area"""
    def area(self):
        """returns the area of square"""
        return self.__size ** 2
