#!/usr/bin/python3
"""A function that prints a concatenated string"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints `My name is <first name> <last name>`
    Args:
        first_name (str): The first part of the fullname.
        last_name (str) : Optional argument for the second half of the fullname
    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
