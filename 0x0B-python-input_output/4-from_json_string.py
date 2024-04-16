#!/user/bin/python3
"""Module that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that convert from a JSON to an object

    Args:
        my_str: a JSON string

    Raises
        Exception: when the string cannot be decoded

    """
    return json.loads(my_str)
