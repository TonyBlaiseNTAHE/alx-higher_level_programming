#!/usr/bin/pyhton3
"""importing module numpy"""
import numpy as np

"""
defining a matrix
args: m_a - the first matrix
      m_b - the second matrix
"""

def lazy_matrix_mul(m_a, m_b):
    """ multipling two matrix using numpy"""
    new_matrix = np.dot(m_a, m_b)
    return new_matrix