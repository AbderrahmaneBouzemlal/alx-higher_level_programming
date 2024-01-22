#!/usr/bin/python3
def no_c(my_string):
    st_list = ""
    my_string = st_list.join([x for x in my_string if x != "c" and x != "C"])
    return my_string
