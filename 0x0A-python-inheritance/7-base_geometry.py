#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """
    Defines a class called BaseGeometry
    """

    def area(self):
        """
        raises Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        Arg:
            name(str): name of the variable
            value(int): value to be validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
