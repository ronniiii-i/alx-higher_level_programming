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

    newText = ""
    for i in range(len(text)):
        if not i == 0 and text[i] == " " and text[i - 1] in ".?:":
            continue
        newText += text[i]
        if text[i] in ".?:":
            newText += "\n\n"
    print(newText, end="")
