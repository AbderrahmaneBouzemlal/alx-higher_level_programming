#!/usr/bin/python3
import json
"""
    This module contains the function save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """

        Args:
        my_obj: object
        filename: file name

    Raises:
        Exception: when the object can't be JSON

    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)
