#!/usr/bin/python3
"""
defining a function that return True
if the object is an instance of,or if the
object is an instance of a class that inherited
from a specified class, otherwise False
"""
def is_kind_of_class(obj, a_class):
    """if statement"""
    if isinstance(obj, a_class):
        return True
    else:
        return False