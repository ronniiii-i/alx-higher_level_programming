#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over the rows of the matrix
    for row in matrix:
        # Initialize a string to represent the row
        row_string = ""

        # Iterate over the elements in the row
        for element in row:
            # Print the element with the appropriate padding
            print("{:d}".format(element), end=" ")
