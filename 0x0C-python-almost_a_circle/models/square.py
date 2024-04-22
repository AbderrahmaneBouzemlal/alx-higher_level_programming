#!/usr/bin/python3
"""This module have the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle and base"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize an object"""
        super(Square, self).__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """a getter for the width"""

        return self.__size

    @size.setter
    def size(self, width):
        """A setter for the width"""

        if type(width) != int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__size = width

    def __str__(self):
        """representation of class"""
        return f"[{Square.__name__}] ({self.id}\
) {self.x}/{self.y} - {self.size}"
