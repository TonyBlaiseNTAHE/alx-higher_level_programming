#!/usr/bin/python3
"""
defining a function that checks if
the object is an instance of,or..
"""


def is_kind_of_class(obj, a_class):
    """if statement"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
