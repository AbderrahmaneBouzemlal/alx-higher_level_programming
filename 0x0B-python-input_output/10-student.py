#!/usr/bin/python3
"""This module
    contains a class Student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to retrieve values"""
        dic = self.__dict__.copy()
        if type(attrs) == list:
            if any(type(x) != str for x in attrs):
                return dic
            else:
                d = {}
                for item in attrs:
                    try:
                        d[item] = dic[item]
                    except KeyError:
                        continue
                return d

        return dic
