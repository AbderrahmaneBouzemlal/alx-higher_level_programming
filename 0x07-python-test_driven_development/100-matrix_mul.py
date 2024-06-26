#!/usr/bin/python3
"""
 Multiply two matrices.

    Args:
        m_a (list of list): The first matrix to be multiplied.
        m_b (list of list): The second matrix to be multiplied.
"""


def matrix_mul(m_a, m_b):
    """
    Returns:
        list of list: The result of multiplying the two matrices.
    """
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
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
