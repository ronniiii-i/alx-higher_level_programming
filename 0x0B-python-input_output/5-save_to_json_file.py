#!/usr/bin/python3
"""
Program that writes an Object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file using a JSON representation """
    if filename = "":
        return
    data = json.dumps(my_obj)
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(data)
