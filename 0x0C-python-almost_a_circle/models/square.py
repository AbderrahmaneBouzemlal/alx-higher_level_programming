#!/usr/bin/python3
"""This module have the square class"""
from models.rectangle import Rectangle # type: ignore


class Square(Rectangle):
    """Square inherits from Rectangle and base"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize an object"""
        super(Square, self).__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """a getter for the width"""
        return self.width

    @size.setter
    def size(self, value):
        """A setter for the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        
    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """representation of class"""
        return f"[{Square.__name__}] ({self.id}\
) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """convert to dictionary"""
        return {'x':getattr(self, "x"),'y':getattr(self, "y"),
                'id':getattr(self, "id"), 'size': getattr(self, "width")}
