#!/usr/bin/python3
import urllib.request
import urllib.error
from sys import argv


try:
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
