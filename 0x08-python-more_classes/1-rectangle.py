#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """
    class that defines a rectangle by private instance attributes:
        width and height
    """
    # how to define private instance attribute with property setter?
    def __init__(self, width=0, height=0):
        """Initialize Variables"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
