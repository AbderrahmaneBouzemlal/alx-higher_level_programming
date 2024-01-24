#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mul = []
    for i in matrix:
        resu = map(lambda x : x * x, i)
        resu = list(resu)
        mul.append(resu)
    return mul
