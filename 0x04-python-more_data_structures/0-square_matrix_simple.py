#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(len(matrix)):
        row_string = []
        for j in range(len(matrix[i])):
            row_string.append((matrix[i][j]) * (matrix[i][j]))
        mat.append(row_string)
    return mat
