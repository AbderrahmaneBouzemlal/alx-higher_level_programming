#!/usr/bin/python3

"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):

    """ Return list of lists """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    matrix_d = []
    length = []
    for ind, i in enumerate(matrix):
        try:
            matrix_v = [round(x/div, 2) for x in i]
        except TypeError:
            raise TypeError('matrix must be a matrix (list of \
                            lists) of integers/floats')
        except ZeroDivisionError:
            raise ZeroDivisionError('division by zero')

        length.append(len(i) - len(matrix[ind - 1]))
        matrix_d.append(matrix_v)
    for b in length:
        if b != 0:
            raise TypeError("Each row of the matrix must have the same size")
    return matrix_d
