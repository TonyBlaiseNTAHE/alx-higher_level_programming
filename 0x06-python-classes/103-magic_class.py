#!/usr/bin/python3
"""defines a class """
import math


class MagicClass:
    """represent a class"""
    def __init__(self, radius=0):
        """initialize the radius"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            """raise error"""
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """returns the area"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """returns the circumference"""
        return 2 * math.pi * self._MagicClass__radius
