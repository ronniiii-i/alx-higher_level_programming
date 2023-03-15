#!/usr/bin/python3
"""Defines a class called Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class called Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__size * self.__size
