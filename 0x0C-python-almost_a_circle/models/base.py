#!/usr/bin/python3
""" In this module we are going to do Base class"""


class Base:
    """A class called base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialize an object of the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
