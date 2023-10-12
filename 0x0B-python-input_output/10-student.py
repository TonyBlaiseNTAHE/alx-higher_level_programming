#!/usr/bin/python3
"""defining a class
"""


class Student:
    """instanciating the class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: A dictionary containing the attributes
            of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    my_dict[key] = self.__dict__[key]
            return my_dict
