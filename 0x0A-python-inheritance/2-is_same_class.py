#!/usr/bin/python3
"""
defining a method called is_same_class
that checks if an object is exactly an
instance
"""


def is_same_class(obj, a_class):
    """if statement"""
    if type(obj) is a_class:
        return True
    else:
        return False
