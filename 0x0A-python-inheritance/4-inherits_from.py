#!/usr/bin/python3
"""
defining function that checks for types
"""


def inherits_from(obj, a_class):
    """if statement"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
