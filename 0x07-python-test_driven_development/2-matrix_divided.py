#!/usr/bin/python3
"""
function that divides element in list of list
args: matrix - the list of lists
      div number to be divided with
"""


def matrix_divided(matrix, div):
    """return new matrix of the division of elements"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size_row = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size_row == 0:
            size_row = len(row)
        elif size_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elm in row:
            if type(elm) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(elm / div, 2) for elm in row]
        new_matrix.append(new_row)
    return new_matrix
