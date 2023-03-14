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


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
