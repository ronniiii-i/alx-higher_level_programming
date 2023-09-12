#!/usr/bin/python3
"""
Program that writes text to a file
"""


def write_file(filename="", text=""):
    """ write to a file and return length of characters written """
    if filename == "":
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
