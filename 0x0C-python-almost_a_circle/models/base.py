#!/usr/bin/python3
# base.py
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to save a list of classes as json"""
        list_dict = []
        if list_objs is not None and type(list_objs) is list:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """return a list from a json string"""
        list_json = []
        if json_string is None or json_string == "":
            return list_json
        list_json = json.loads(json_string)
        return list_json

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle" or cls.__name__ == "Square":
                new = cls(1, 1)
            else:
                new = cls(1)
                new.update(**dictionary)
            return new

