#!/usr/bin/python3
""" importing json module
"""

import json

"""module called to_json_string that
retursn the JSON representation of an object
"""


def to_json_string(my_obj):
    """ function that returns the JSON
        representation of an object
        args: my_obj - the object
    """
    return json.dumps(my_obj)
