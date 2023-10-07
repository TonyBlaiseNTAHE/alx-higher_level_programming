#!/usr/bin/python3
"""
function that prints Square with the character #.
args: size  - the size of the square
"""


def print_square(size):
    """prints a square with "#"'s that has a length of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
