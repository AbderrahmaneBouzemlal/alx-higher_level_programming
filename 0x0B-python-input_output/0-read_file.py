#!/usr/bin/python3
"""This module contains one function read_file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        read_data = file.read()
