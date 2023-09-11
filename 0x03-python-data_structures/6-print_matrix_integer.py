#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if j == num_cols - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
            print()
    else:
        print()
