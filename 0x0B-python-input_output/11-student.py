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
            for attr in attrs:
                if attr in self.__dict__.keys():
                    my_dict[attr] = self.__dict__[attr]
            return my_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        """
        current_dict = self.__dict__
        for attr in json.keys():
            for current_attr in current_dict:
                if attr == current_attr:
                    current_dict[current_attr] = json[attr]
        return current_dict
