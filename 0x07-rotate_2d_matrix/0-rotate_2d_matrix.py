#!/usr/bin/python3
"""
Module that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """function that rotates a 2D matrix 90 degrees clockwise
    Args:
        matrix: n x n 2D matrix
    """
    n = len(matrix)
    for c in range(int(n / 2)):
        b = (n - c - 1)
        for d in range(c, b):
            e = (n - 1 - d)
            f = matrix[c][d]
            matrix[c][d] = matrix[e][c]
            matrix[e][c] = matrix[b][e]
            matrix[b][e] = matrix[d][b]
            matrix[d][b] = f