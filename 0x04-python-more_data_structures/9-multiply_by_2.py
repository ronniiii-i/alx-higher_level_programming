#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_key = {}
    for i in sorted(a_dictionary):
        new_key = {i: a_dictionary.get(i) * 2}
        a_dictionary.update(new_key)
    return a_dictionary
