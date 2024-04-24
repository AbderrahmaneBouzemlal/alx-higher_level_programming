#!/usr/bin/python3
""" In this module we are going to do Base class"""
import json


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

    def to_json_string(list_dictionaries):
        """
            it converts the list of dictionaries of the class to a 
            json object
            returns a json object
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
