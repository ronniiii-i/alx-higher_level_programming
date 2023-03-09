#!/usr/bin/python3
"""Defines a function that prints 2 new lines after . , ? and :"""


def text_indentation(text):
    """
    Prints 2 new lines after the characters.,? and :
    Arg:
        text (string): text to indent
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n")
          .replace(", ", ",\n\n").replace(": ", ":\n\n"))
