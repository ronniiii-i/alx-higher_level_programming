#!/bin/bash
# Retrieves the byte size of the HTTP response header for a URL
curl -s -w '%{http_code}\n' -o /dev/null $1
