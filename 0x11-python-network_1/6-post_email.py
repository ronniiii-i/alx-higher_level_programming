#!/usr/bin/python3
"""Python script that sends a POST req using request"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
