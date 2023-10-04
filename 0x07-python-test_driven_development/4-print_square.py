#!/usr/bin/python3
"""
function that prints Square with the character #.
args: size  - the size of the square
"""


def print_square(size):
    """if statement"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
