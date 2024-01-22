#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    if length % 2 == 0:
        for element in range(0, length- 1):
            tmp = my_list[element]
            my_list[element] = my_list[-element-1]
            my_list[-element-1] = tmp
    else:
        for element in range(0, length - 2):
            tmp = my_list[element]
            my_list[element] = my_list[-element-1]
            my_list[-element-1] = tmp
    for i in my_list:
        print(i)
