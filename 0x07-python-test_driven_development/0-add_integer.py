#!/usr/bin/python3
"""
module add_integer
arguments are a and b
returns sum of a and b
"""
def add_integer(a, b=98):
    """
    add_integer
    """
    if type(a) not in [int, float]:
        """ raise Error"""
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        """raise Error"""
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
