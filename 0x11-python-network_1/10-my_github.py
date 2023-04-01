#!/usr/bin/python3
"""Python script that usues github api to display id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    basic = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get("id"))
