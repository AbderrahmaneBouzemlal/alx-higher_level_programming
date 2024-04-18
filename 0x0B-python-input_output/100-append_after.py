#!/usr/bin/python3
"""This module contains The function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """appending to a file after a certain line"""
    with open(filename, "r", encoding="utf-8") as file:
        file.seek(0)
        data = file.readlines()
        for indx, line in enumerate(data):
            if search_string in line:
                if indx == len(data):
                    data.append(new_string)
                else:
                    data.insert(indx + 1, new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(data)
