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
        """"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
