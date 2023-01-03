#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is dict:
        first = list(a_dictionary.keys())[0]
        store = a_dictionary.get(first)
        new_dict = first
        for i in sorted(a_dictionary):
            if store > a_dictionary.get(i):
                continue
            else:
                store = a_dictionary.get(i)
                new_dict = i
        return new_dict
    else:
        return None
