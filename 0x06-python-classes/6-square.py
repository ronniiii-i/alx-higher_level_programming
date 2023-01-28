#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square class with a private instance attribute `size`."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with optional size parameter.

        Args:
            size (int, optional): Size of the Square. Default is 0.
            position (tuple, optional): Position of the Square. Default is 0,0

        Raises:
            TypeError: If the value of size is not an integer.
            ValueError: If the value of size is less than 0.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter method for position

        Returns:
            tuple: Position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.

        Args:
            value (tuple): New value for position.

        Raises:
            TypeError: If value is not two positive integers
        """
        if not isinstance(value, tuple)\
                or len(value) != 2\
                or (value[0] or value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square to stdout."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
