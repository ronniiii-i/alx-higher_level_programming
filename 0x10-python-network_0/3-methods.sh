#!/bin/bash
# Script that list all possibe HTTP methods for a URL
curl -sIX OPTIONS "$1" | grep "methods\|Methods" | cut -d " " -f 2-
