#!/usr/bin/python3
"""
This module have one function class_to_json
"""


def class_to_json(obj):
    """
    class_to_json function that converts from class to json
        obj: the class instance
    """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
