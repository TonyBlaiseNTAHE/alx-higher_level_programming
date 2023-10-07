#!/usr/bin/python3

"""
defining a matrix
args: m_a - the first matrix
      m_b - the second matrix
"""


def matrix_mul(m_a, m_b):
    """ multiplying two matrices"""
    row1 = len(m_a)
    cols1 = len(m_a[0])
    row2 = len(m_b)
    cols2 = len(m_b[0])
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    for j in m_a:
        if type(j) is not list:
            raise TypeError("m_a must be a list of lists")
    if row1 == 0:
        raise TypeError("m_a can't be empty")
    if row2 == 0:
        raise TypeError("m_b can't be empty")
    for elm in m_a:
        for i in elm:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for elmt in m_b:
        for i in elmt:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for element in m_a:
        if len(element) != cols1:
            raise TypeError("each row of m_a must be of the same size")

    for element in m_b:
        if len(element) != cols2:
            raise TypeError("each row of m_b must be of the same size")
    if cols1 != row2:
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for _ in range(cols2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
