#!/usr/bin/python3
"""
this module contains two functions save_to_json_file
and load_from_json_file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add-item.json'

if os.path.isfile(filename):
    data = load_from_json_file(filename)
else:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(data, filename)
