#!/bin/bash
# Retrieves the status code for a URL
curl -s -w '%{http_code}' -o /dev/null $1
