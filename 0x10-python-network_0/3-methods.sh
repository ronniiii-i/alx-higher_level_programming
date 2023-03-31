#!/bin/bash
# Script that list all possibe HTTP methods for a URL
curl -sIX OPTIONS "$1" | grep "allow\|Allow" | cut -d " " -f 2-
