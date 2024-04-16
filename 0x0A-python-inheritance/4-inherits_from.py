#!/usr/bin/python3
"""
This module contains a function called inherits_from
"""


def inherits_from(obj, a_class):
    """return True if the object is an of a class inherited
    from specified class"""
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
