#!/bin/bash
# Script that posts data from a json file to a URL
curl -sX POST -d @"$2" "$1"