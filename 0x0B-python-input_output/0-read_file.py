#!/usr/bin/python3
"""This module contains one function read_file"""


def read_file(filename=""):
    """return the data in the file"""
    with open(filename, "r") as file:
        print(file.read())
