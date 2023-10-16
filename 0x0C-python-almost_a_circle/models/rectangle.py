#!/usr/bin/python3
"""importing module base from models package
"""
from models.base import Base

"""class called Rectangle
"""


class Rectangle(Base):
    """class constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instanciating attribute
        """
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validator(self, name, value, less_eq):
        """validator(validate values and types)"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if less_eq:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """display the rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return string representaion"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """returns the dictionary representation of Rectangle"""
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }

    def update(self, *args, **kwargs):
        """printing arguments"""
        if args:

            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'width':
                        self.__width = value
                    elif key == 'height':
                        self.__height = value
                    elif key == 'x':
                        self.__x = value
                    elif key == 'y':
                        self.__y = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        self.validator("width", width, True)
        self.__width = width

    @property
    def height(self):
        """width getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.validator("height", height, True)
        self.__height = height

    @property
    def x(self):
        """width getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.validator("x", x, False)
        self.__x = x

    @property
    def y(self):
        """width getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.validator("y", y, False)
        self.__y = y
