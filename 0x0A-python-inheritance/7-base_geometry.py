#!/usr/bin/python3
"""
This module contains a class BaseGeometry
"""


class BaseGeometry:
    """A class"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the values to be integer or bigger than 0"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
