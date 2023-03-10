#!/usr/bin/python3
"""Define a function that strings BestSchool n time"""


def magic_string():
    """Return a string "BestSchool" n times the number of the iteration

    Returns:
    A string with the format "BestSchool, BestSchool, ..., BestSchool"
    with n-1 commas and n "BestSchool" strings, where n is the number
    of times the function has been called.
    """
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.count
