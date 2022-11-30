#!/usr/bin/python3
def islower(c):
    temp = ""
    test = False
    for i in range(97, 123):
        if c != chr(i):
            continue
        else:
            temp = chr(i)    
    if temp == "":
        return False
    else:
        return True
