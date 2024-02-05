#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_count = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
            real_count += 1
        except IndexError:
            print()
            return real_count
    print()
    return real_count
