#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
matrix_mul = __import__("100-matrix_mul").matrix_mul
# print("__________")
# print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print("mine")
# print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print("__________")
# print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
# print("mine")
# print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
# print("__________")
# print(lazy_matrix_mul([["say", "my"], ["name", "heisenberg"]], [[1, 2], [1, 2]]))
m_a = [[1, 2, 3],
       [4, 5, 6]]

m_b = [[7, 8],
       [9, 10],
       [11, 12],
       [13, 14]]
try:
    print("mine")
    print(matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
