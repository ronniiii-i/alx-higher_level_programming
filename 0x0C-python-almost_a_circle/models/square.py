#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the new Square (both width and height).
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a custom string representation of the Square.

        Returns:
            str: A string in custom format
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Updates instance attributes via no-keyword & keyword args.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of Rectangle
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
