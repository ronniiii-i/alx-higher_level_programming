#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"{string} {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"{string} {number:d} is {last_digit:d} and is 0")
else:
    print(f"{string} {number:d} is {last_digit:d} and is less than 6 and not 0")
