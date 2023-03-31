#!/bin/bash
# Script that take URL, sends GET request and displays response body
curl -sH "X-School-User-Id:98" -X GET "$1"