#!/usr/bin/python3
"""A square printing function"""


def print_square(size):
    """
    A function that prints a square of the given size
    Args:
        size (int): dimensions of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is float and less than 0
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
