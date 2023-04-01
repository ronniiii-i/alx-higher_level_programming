#!/usr/bin/python3
"""Python script that fetches from URL using requests"""
import requests


r = requests.get("https://alx-intranet.hbtn.io/status")
# print(r.content)
print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r.content))
