#!/usr/bin/python3
"""importing json
"""
import json

"""module containing a class called Student
and a method called to_json
"""


class Student:
    """instanciating the class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: A dictionary containing the attributes
            of the Student instance.
        """
        return self.__dict__
