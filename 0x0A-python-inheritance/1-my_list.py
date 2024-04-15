#!/usr/bin/python3
""" In this module there is a class called MyList"""


class MyList(list):
    """This class is an implementation of a list-like"""
    def __init__(self):
        """initialization of the list by subclassing the list class"""
        super().__init__(self)

    def print_sorted(self):
        """method to sort the elements of the list"""
        x = sorted(self)
        print(x)
