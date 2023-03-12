#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and
methods of an object"""


def lookup(obj):
    """
    Arg:
        obj: the object to look up the attributes and methods of
    Returns the list of available attributes and methods of an object
    """
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    return attributes, methods
