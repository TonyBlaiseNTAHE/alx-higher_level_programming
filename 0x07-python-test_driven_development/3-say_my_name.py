#!/usr/bin/python3
"""
function called say_my_name that prints your names
args: first_name - the first name
      last_name - second name
"""


def say_my_name(first_name, last_name=""):
    """if statements"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    elif last_name is None:
        print("My name is {} ".format(first_name))
    print("My name is {} {}".format(first_name, last_name))
