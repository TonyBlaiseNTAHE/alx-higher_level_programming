#!/usr/bin/python3
"""
defines a class
"""


class Rectangle:
    """Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing retangle attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__heigth = value

    def area(self):
        """return the area"""
        return self.__heigth * self.__width

    def perimeter(self):
        """returns the perimeter"""
        return 2 * (self.__heigth + self.__width)

    def __str__(self):
        """defines print()"""
        if self.__heigth == 0 or self.__width == 0:
            return ""
        else:
            res = ""
            for i in range(self.__heigth):
                for j in range(self.__width):
                    res += str(self.print_symbol)
                res += "\n"
        return res[:-1]

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__heigth})'

    def __del__(self):
        """print a message if the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """return new instance"""
        return cls(size, size)
