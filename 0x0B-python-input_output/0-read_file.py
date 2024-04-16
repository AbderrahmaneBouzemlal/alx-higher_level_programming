#!/usr/bin/python3
"""This module contains one function read_file"""


def read_file(filename=""):
    """return the data in the file"""
    with open(filename, "r", encoding="utf-8") as file:
        for i in file:
            if i == "\n":
                continue
            print(i, end="")
        print()
