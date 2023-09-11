#!/usr/bin/python3
"""
Defines a function that checks if an obj is an intance of a class
"""


def inherits_from(obj, a_class):
    """
    Checks  if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj: the object to check
        a_class: the class to check against
    Returns:
        True if the object is an instance of a class that inherited
        Otherwise, False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
