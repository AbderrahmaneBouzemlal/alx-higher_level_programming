#!/usr/bin/python3
"""
this module contains two functions save_to_json_file
and load_from_json_file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
save_to_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import json
FILE = "add_item.json"


def main():
    data = sys.argv[1]
    save_to_json_file(data, FILE)
