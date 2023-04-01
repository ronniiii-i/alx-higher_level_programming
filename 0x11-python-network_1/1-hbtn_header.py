#!/usr/bin/python3
"""Python script that sends a req to a url and displays a header value"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
