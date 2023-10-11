#!/usr/bin/python3
"""modula containing function called
class_to_json
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary with s
    erializable data structures for JSON serialization.
    Args:
        obj: An instance of a class with serializable
        attributes (list, dictionary, string, integer, boolean).
    Returns:
        dict: A dictionary representation of the object
        with serializable attributes.
    """
    serialized_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, bool, list, dict, str)):
            serialized_dict[key] = value
    return serialized_dict
