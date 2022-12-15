#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if i == chr(99) or i == chr(67):
            continue
        else:
            new += i
    return new
