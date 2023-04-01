#!/usr/bin/python3
"""Python script that sends a POST req with a param"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if argv[1] is None:
        params = {"q": ""}
    else:
        params = {"q": argv[1]}

    r = requests.post(url, data=params)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
