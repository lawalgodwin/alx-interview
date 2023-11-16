#!/usr/bin/python3
"""A module containing the logic for retating a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degree clock-wise"""
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    # Reverse the order of each row in the transposed matrix
    for row in matrix:
        row.reverse()
