#!/usr/bin/python3
"""Representing a class and its properties"""


class Square:
    """Defining a class called Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(elem, int) and elem > 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with position"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
