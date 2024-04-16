#!/usr/bin/python3
"""
This module contains two classes BaseGeometry and Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class represent the rectangle"""
    def __init__(self, width, height):
        """initialize the object of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
