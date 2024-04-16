#!/usr/bin/python3
"""This module contains the function to_json_string"""
import json


def to_json_string(my_obj):
    """Function thats convert to json object

    Args:
        my_obj: the object to be converted
    raises:
        when the Object is of type set is not JSON serializable
    """
    return json.dumps(my_obj)
