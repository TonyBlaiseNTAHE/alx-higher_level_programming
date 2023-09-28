#!/usr/bin/python3
"""Representing a class Square and its proporties"""


class Square:
    """defining a function called __init"""
    def __init__(self, size=0):
        """Initialise the size"""
        self.__size = size

    """defining size property"""
    @property
    def size(self):
        """Returns the Square's size"""
        return self.__size

    @size.setter
    def size(self, value):
        """if statement"""
        if not isinstance(value, int):
            """ raise Error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise Error """
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """defining area function"""
    def area(self):
        """Returns the area of square"""
        return self.__size ** 2
