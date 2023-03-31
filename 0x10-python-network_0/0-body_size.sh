#!/bin/bash
# Retrieves the byte size of the HTTP response header for a URL
curl -s -w '%{size_download}' -o /dev/null $1