#!/usr/bin/python3
"""Python script that prints out 10 most recent commits using github api"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name"))
                )
    except IndexError:
        pass
