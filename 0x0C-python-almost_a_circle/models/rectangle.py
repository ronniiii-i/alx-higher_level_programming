#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def set_width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): The new width value.
        """
        self.__width = width

    @property
    def get_height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def set_height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): The new height value.
        """
        self.__height = height

    @property
    def get_x(self):
        """
        Get the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @width.setter
    def set_x(self, x):
        """
        Set the x-coordinate of the rectangle.

        Args:
            x (int): The new x-coordinate value.
        """
        self.__x = x

    @property
    def get_y(self):
        """
        Get the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @width.setter
    def set_y(self, y):
        """
        Set the y-coordinate of the rectangle.

        Args:
            y (int): The new y-coordinate value.
        """
        self.__y = y
