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

    def area(self):
        """returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return the perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """define print function"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            result = ""
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    result += "#"
                result += "\n"
            return result
