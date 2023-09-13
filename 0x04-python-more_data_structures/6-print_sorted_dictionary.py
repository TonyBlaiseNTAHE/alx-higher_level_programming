#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        sorted_dict = dict(sorted(a_dictionary.items()))
        for key, value in sorted_dict.items():
            print("{:s}: {}".format(key, value))
    else:
        print("Invalid dictionary or None")
