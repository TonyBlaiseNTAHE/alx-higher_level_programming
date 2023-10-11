#!/usr/bin/python3
"""importing json module
"""

import json

""" module containing function called
save_to_json_file
"""


def save_to_json_file(my_ojb, filename):
    """writes an oject to text file, using
       a JSON representation
       args: my_obj - the object
             filename - the filename
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_ojb))
