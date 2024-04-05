#!/usr/bin/python3


"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().

"""


def add_integer(a, b=98):

    """Return the sum of a and b, two integers of float"""

    allowed_types = [int, float]

    if type(a) not in allowed_types:
        raise TypeError("a must be an integer")
    if type(b) not in allowed_types:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
