#!/usr/bin/python3

"""
This is the "3-say_my_name" module.

The 3-say_my_name module supplies one function, say_my_name().

"""


def say_my_name(first_name, last_name=""):

    """ Return string """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
