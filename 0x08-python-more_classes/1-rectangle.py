#!/usr/bin/python3
"""
This is the "0-rectangle" module.

The 0-rectangle module supplies one function, rectangle().
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value for the width regarding some restrictions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """serve as a getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value for the height regarding some conditions"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
