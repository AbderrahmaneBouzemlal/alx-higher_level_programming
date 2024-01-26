#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_tuples = 0
    sum_t = 0
    length = len(my_list)
    if length == 0:
        return 0
    result = map(lambda x: x[0] * x[1], my_list)
    result = list(result)
    for mul in result:
        sum_tuples += mul
    avrage = map(lambda x: x[1], my_list)
    for i in avrage:
        sum_t += i
    avg = sum_tuples / sum_t
    return avg
