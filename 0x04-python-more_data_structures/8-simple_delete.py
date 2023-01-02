#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    c = 0
    for i in sorted(a_dictionary):
        if i == key:
            a_dictionary.pop(key)
    return a_dictionary
