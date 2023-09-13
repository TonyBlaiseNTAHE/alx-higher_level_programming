#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
