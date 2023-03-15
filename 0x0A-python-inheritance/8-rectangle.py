#!/usr/bin/python3
"""Defines a class"""


class Rectangle(BaseGeometry):
    """
    Defines a class called Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance.
        Args:
            width (int): The width of the Rectangle instance.
            height (int): The height of the Rectangle instance.
        """
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
