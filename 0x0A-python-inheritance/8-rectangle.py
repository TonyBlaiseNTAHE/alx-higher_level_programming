#!/usr/bin/python3
"""
importing module 7-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""defines a class"""


class Rectangle(BaseGeometry):
    """defining contructor"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
