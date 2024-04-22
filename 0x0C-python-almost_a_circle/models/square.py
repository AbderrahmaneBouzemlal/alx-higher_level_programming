#!/usr/bin/python3
"""This module have the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle and base"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize an object"""
        super(Square, self).__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = self.width

    def __str__(self):
        """representation of class"""
        return f"[{Square.__name__}] ({self.id}\
) {self.x}/{self.y} - {self.size}"
