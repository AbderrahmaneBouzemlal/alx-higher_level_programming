#!/usr/bin/python3
"""
This module contains two classes Square and Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialize the object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)
