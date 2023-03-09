#!/usr/bin/python3
"""A matrix division function"""


def matrix_divided(matrix, div):
    """
     Divides a matrix by a given number and returns a new matrix
     Args:
        matrix (list of lists): A matrix represented as a list of lists.
        div (int/float): The number to divide each element of the matrix by
     Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If div is not a number.
        TypeError: If matrix rows are not of equal length
        ZeroDivisionError: If div is zero.
     Returns:
        A new matrix with each element divided by the given number.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element, (int, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
 floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return new_matrix
