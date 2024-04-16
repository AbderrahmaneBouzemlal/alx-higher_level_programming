#!/usr/bin/python3
"""This module have only one function append_write"""


def append_write(filename="", text=""):
    """Function that append to the end of a file file

    Args:
        filename: filename
        text: the text to be appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
