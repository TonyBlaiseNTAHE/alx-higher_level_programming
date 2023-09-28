#!/usr/bin/python3
""" Representing a class Square and its property"""


class Square:
    """ define function called __init__"""
    def __init__(self, size=0):
        """initialize square's size"""
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """if statement"""
        if not isinstance(value, int):
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """Raise Error """
            raise ValueError("size must be >= 0")
        else:
            """initializing the size"""
            self.__size = value
    """defining a function called print"""
    def my_print(self):
        """if statement"""
        if self.__size == 0:
            """printing an empty line"""
            print("")
        else:
            """initialize the size"""
            count = self.__size
            """for loop to print the square with charater"""
            for i in range(count):
                for j in range(count):
                    print("#", end="")
                print()
