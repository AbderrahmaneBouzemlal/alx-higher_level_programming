#!/usr/bin/python3
"""
This module contains two classes BaseGeometry Rectangle
"""


class BaseGeometry:
    """A class with some validations"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the values to be integer or bigger than 0"""
        if value.__class__ != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class represent the rectangle"""
    def __init__(self, width, height):
        """initialize the object of rectangle"""
        self.__width = width
        self.__height = height
        super().integer_validator(self, self.__width)
        super().integer_validator(self, self.__height)
