#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for k, v in a_dictionary.items():
        b_dictionary[k] = a_dictionary[k] * 2
    return b_dictionary
