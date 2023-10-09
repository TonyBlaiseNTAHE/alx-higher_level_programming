#!/usr/bin/python3
"""
defining a function that check if
an object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """if statement"""
    if type(obj) is a_class:
        return True
    else:
        return False
