#!/usr/bin/python3
"""
defines a function that return the list
of available attributes and methods of an object
"""


def lookup(obj):
    """return the list"""
    return dir(obj)
