#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
matrix and div arguments
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in the matrix by div
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size_row = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size_row is None:
            size_row = len(row)
        elif size_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elm in row:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elm / div, 2) for elm in row] for row in matrix]
