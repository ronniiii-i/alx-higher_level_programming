#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and
methods of an object"""


def lookup(obj):
    """
    Arg:
        obj: the object to look up the attributes and methods of
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
