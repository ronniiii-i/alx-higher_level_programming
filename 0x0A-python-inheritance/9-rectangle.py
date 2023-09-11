#!/usr/bin/python3
"""Defines a class called Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class called Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height
