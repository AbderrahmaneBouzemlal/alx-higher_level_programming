#!/usr/bin/python3
"""This module contains the function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle
    """
    res = []
    arr = []

    if n <= 0:
        return res

    for i in range(n):
        res.append([1])
        arr = res[i]
        for j in range(1, i + 1):
            if j == i:
                arr.append(1)
                continue
            arr.append(res[i-1][j] + res[i-1][j-1])
    return res
