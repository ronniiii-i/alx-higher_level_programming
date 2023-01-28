#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square class with a private instance attribute `size`."""

    def __init__(self, size=0):
        """
        Initializes a Square object with optional size parameter.

        Args:
            size (int, optional): Size of the Square. Default is 0.

        Raises:
            TypeError: If the value of size is not an integer.
            ValueError: If the value of size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: Size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): New value for size.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
