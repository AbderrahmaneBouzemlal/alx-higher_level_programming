#!/usr/bin/python3
import json
"""
This module have one function class_to_json
"""


def class_to_json(obj):
    """
    class_to_json function that converts from class to json
        obj: the class instance
    """
    j_string = json.dumps(vars(obj), default=lambda x: x. __dict__)
    return json.loads(j_string)
