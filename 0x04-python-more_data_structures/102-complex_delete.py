#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        if value:
            new_dict = [key for key, val in a_dictionary.items() if val == value]
            for key in new_dict:
                del a_dictionary[key]
        else:
            return a_dictionary
        return a_dictionary
    else:
        return None
