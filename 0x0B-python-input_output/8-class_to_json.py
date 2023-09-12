#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object"""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure"""
    return obj.__dict__
