#!/usr/bin/python3
"""
This module contains two classes Square and Rectangle
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

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):
    """representation of a square"""
    def __init__(self, size):
        """initialize the object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculation of the area of the square"""
        return (self.__size ** 2)
