#!/usr/bin/python3
"""Python script that sends POST req with email param to a URL"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    data = urllib.parse.urlencode(email).encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        print("Your email is: {}".format(response.read().decode()))
