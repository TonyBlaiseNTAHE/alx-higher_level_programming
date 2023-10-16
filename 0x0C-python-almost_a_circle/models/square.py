#!/usr/bin/pyhton3
"""importing pacage
"""
from models.rectangle import Rectangle

""" Sqaure Class child of Rectangle class
"""


class Square(Rectangle):
    """Square contructor(__init__)
       agrs: size - the size of a square
            x - a variable
            y - a variable
    """
    def __init__(self, size, x=0, y=0):
        super().__init__(width=size, height=size, x=x, y=y)
        self.__height = size
        self.__width = size
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        self.validator("width", size, True)
        self.__width = size

    def update(self, *args, **kwargs):
        """updating methos"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.__x = value
                    elif key == 'y':
                        self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.__x,
            'y': self.__y
        }
