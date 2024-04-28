#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response header.")
