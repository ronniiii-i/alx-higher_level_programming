#!/usr/bin/python3
"""
Defines a function that checks if object is an instance of a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a specified class
    Returns:
        True: if it is exactly an instance of specified class
        False: otherwise
    """
    return isinstance(obj, a_class)
