#!/usr/bin/python3
"""
defines a class
"""


class Rectangle:
    """defines a method named __init__"""
    def __init__(self, width=0, height=0):
        """initialise the attributes"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("width must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("height must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
