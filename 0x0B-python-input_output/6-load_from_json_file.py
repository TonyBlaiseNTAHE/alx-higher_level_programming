#!/usr/bin/python3
"""importing json module
"""

import json

"""defining a function called
load_from_json that creates an Object from
a "JSON file"
"""


def load_from_json_file(filename):
    """creates an Oject from "JSON file"
       args: filename - the file name
       returns: object
    """
    with open(filename, "r", encoding="utf") as file:
        f = file.read()
        return json.loads(f)
