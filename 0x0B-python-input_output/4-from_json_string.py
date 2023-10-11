#!/usr/bin/python3
"""importing a module called json
"""

import json


"""defining a function that returns an object
"""


def from_json_string(my_str):
    """ returns an object from json string
        args: my_str - json string
    """
    return json.loads(my_str)
