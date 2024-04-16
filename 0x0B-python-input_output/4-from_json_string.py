#!/user/bin/python3
"""This module contains the function from_json_string"""
import json


def from_json_string(my_str):
    """ Function that convert from a JSON to an object

        Args:
            my_str: a JSON string

        Raises
            Exception: when the my_str is not a JSON String

    """
    j = json.loads(my_str)
    return json.dumps(j, sort_keys=True)
