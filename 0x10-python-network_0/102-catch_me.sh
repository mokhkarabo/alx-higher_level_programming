#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me with curl, send POST request with empty data
response=$(curl -s -X POST http://0.0.0.0:5000/catch_me --data "")

# Print the response body
echo "$response" | grep -o "You got me!"
