#!/usr/bin/python3

"""This is the "101-lazy_matrix_mul" module.
The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul().
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return the multiplication of the matrixes"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or all(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or all(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    for matrix in [m_a, m_b]:
        for row in matrix:
            for val in row:
                if not isinstance(val, (int, float)):
                    if matrix is m_a:
                        raise TypeError(
                            "m_a should contain only integers or floats")
                    else:
                        raise TypeError(
                            "m_b should contain only integers or floats")

    row_size_a = len(m_a[0])
    row_size_b = len(m_b[0])
    if (any(len(row) != row_size_a for row in m_a)
            or any(len(row) != row_size_b for row in m_b)):
        raise TypeError("each row of m_a must be of the same size"
                        if any(len(row) != row_size_a for row in m_a)
                        else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_a = np.array(m_a)
    m_b = np.array(m_b)
    m_c = np.dot(m_a, m_b)
    return m_c
