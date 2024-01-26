#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    dic = list (a_dictionary)
    for k in dic:
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return a_dictionary
