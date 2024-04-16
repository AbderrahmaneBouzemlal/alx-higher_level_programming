#!/usr/bin/python3
"""This module contains one function read_file"""


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    with open(filename, "r", encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
