#!/usr/bin/python3
"""Defines a function that prints a square with the character #"""


def print_square(size):
    """
    Prints a square with the character #
    Arg:
        size (int): the size of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        TypeError: If size is a float and less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
