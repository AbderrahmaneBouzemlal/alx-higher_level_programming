#!/user/bin/python3
"""This module contains the function from_json_string"""
# import json


def from_json_string(my_str):
    """ Function that reads from a file

        Args:
            my_str: a JSON string

        Raises
            Exception: when the my_str is not a JSON String

    """
    return json.loads(my_str)
