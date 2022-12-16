#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # # Check if the matrix is empty
    for row in matrix:
        # Initialize a string to represent the row
        row_string = ""

        # Iterate over the elements in the row
        for element in row:
            # Add the element to the row string
            row_string += "{} ".format(element)

        # Print the row string
        print(row_string)
