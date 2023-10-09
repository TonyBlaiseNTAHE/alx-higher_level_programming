#!/usr/bin/python3
"""
defining a function that return the list
of available attributes
"""


def lookup(obj):
    """return the list of object"""
    return dir(obj)
