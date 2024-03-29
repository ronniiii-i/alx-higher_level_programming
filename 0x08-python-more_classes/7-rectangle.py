#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """
    class that defines a rectangle by private instance attributes:
        width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Variables"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to det area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method to get perimiter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2*self.__width)+(2*self.__height))

    def __str__(self):
        """method to return string representation of rectangle"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            string += "\n"
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """returns string representation of rectangle"""
        return "Rectangle({}, {})".format(str(self.__width), str(self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
