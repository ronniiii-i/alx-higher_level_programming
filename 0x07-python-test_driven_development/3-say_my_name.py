#!/usr/bin/python3
"""Defines a function that concatenates string"""


def say_my_name(first_name, last_name=""):
    """
    Prints a concatenated string
    Args:
        first_name (string): Person's first name
        last_name (string): Person's last name
    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("Hello {} {}".format(first_name, last_name))
    # print(f"Hello {first_name} {last_name}")


say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
