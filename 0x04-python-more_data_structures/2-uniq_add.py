#!/usr/bin/python3
def uniq_add(my_list=[]):
    doubles = []
    result = 0
    for number in my_list:
        if number not in doubles:
            result += number
            doubles.append(number)
    return(result)
