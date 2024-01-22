#!/usr/bin/python3
def no_c(my_string):
    string_list = ""
    my_string = string_list.join([x for x in my_string if x != "c" and x != "C"])
    return my_string
