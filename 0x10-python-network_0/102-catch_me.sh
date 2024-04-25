#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me with curl, sending POST request with empty data
response=$(curl -s -X POST http://0.0.0.0:5000/catch_me --data "")

# Check if the response contains the message "You got me!"
if [[ $response == *"You got me!"* ]]; then
    # If it does, exit successfully
    exit 0
else
    # If it doesn't, exit with an error
    exit 1
fi
