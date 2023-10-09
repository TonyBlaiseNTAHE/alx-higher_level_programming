#!/usr/bin/python3
"""
defines a method called inherits
"""


def inherits_from(obj, a_class):
    """if statement"""
    if type(obj) is not a_class:
        return True
    return False
