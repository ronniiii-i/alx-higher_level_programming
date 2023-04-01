#!/usr/bin/python3
"""Python script that fetches from URL using requests"""
import requests


if __name__ == '__main__':
    r = requests.get("https://alx-intranet.hbtn.io/status")
    # print(r.content)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
