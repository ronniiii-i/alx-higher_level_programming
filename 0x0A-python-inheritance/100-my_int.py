#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """
    A class that inherits from int and has the operators == and != inverted
    """

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
