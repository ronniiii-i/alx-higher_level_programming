#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in sorted(a_dictionary):
        new_key = {i: a_dictionary.get(i) * 2}
        new_dict.update(new_key)
    return new_dict
