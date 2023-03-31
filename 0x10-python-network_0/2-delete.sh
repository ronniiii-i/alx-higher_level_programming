#!/bin/bash
# A script that deletes the URL passed as an arg
curl -sX DELETE "$1"
