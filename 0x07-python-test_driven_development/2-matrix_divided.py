#!/usr/bin/python3
"""
function that divides element in list of list
args: matrix - the list of lists
      div number to be divided with
"""


def matrix_divided(matrix, div):
    """if statements"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    size_row = len(matrix[0])
    for row in matrix:
        if len(row) != size_row:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_list.append(new_row)
    return new_list
