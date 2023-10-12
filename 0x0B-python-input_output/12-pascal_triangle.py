#!/usr/bin/python3
"""defining a function called
pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to row n.
    Args:
        n (int): Number of rows in Pascal's Triangle.
    Returns:
        list of lists: Pascal's Triangle up to row n.
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    return triangle
