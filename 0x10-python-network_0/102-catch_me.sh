#!/bin/bash
# Script that makes a req to a url for a response
curl -sLX PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
