#!/usr/bin/python3
import numpy as np
"""
This is the "101-lazy_matrix_mul" module.

The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul().

"""

def lazy_matrix_mul(m_a, m_b):
    """return the multiplication of the matrixes"""
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    m_c = np.dot(m_a, m_b)
    return m_c
