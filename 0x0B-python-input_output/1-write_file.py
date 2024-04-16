#!/usr/bin/python3
"""This module have only one function write_file"""


def write_file(filename="", text=""):
    """Function that writes to a file

    Args:
        filename: filename
        text: the text to be written

    Raises
        Exception: when the file can be opened
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
