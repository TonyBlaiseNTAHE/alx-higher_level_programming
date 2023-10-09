#!/usr/bin/python3
"""
definning a class called Mylist
that inherits from built-in class list
"""


class MyList(list):
    """defining the constructor"""
    def __init__(self):
        super().__init__()
    """definning method to print in sorted order"""
    def print_sorted(self):
        print(sorted(self))
