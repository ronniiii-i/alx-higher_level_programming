#!/usr/bin/python3
"""Defines class that inherits from list"""


class MyList(list):
    """
    Class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Sorts the list and prints the sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
