#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key, value in a_dictionary.items():
        if key:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
            print("{:s}: {}".format(key, value))
