#!/usr/bin/python3
"""This module contains The function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """appending to a file after a certain line"""
    with open(filename, "a+", encoding= "utf-8") as file:
        for line in file:
            if search_string in line:
                file.write(new_string)
