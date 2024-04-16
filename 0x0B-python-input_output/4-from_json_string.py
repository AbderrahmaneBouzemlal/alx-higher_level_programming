#!/user/bin/python3
"""This module contains the function from_json_string"""
import json


def from_json_string(my_str):
    """returns a list from a json string"""
    return json.loads(my_str)
