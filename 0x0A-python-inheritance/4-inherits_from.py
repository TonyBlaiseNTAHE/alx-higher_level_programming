#!/usr/bin/python3
"""
defines a method called inherits
"""


def inherits_from(obj, a_class):
    """if statement"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
