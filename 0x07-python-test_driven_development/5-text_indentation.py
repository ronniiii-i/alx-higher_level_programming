#!/usr/bin/python3
"""A function that prints new lines after certain characters"""


def text_indentation(text):
    """
    Prints the given string with 2 new lines after the characters ., ? and :
    Args:
        text(str): given string
    Raises:
        TypeError: if text is not a string
    """
    newText = ""

    for i in range(len(text)):
        """
        iterates through the indices of characters in the input string
        """
        if not i == 0 and text[i] == " " and text[i - 1] in ".?:":
            continue
        newText += text[i]
        if text[i] in ".?:":
            newText += "\n\n"
    print(newText, end="")
