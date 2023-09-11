#!/usr/bin/python3
"""Defines a function that adds new attributr to an object if possible"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the new attribute to.
        name (str): The name of the new attribute.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute added.

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
