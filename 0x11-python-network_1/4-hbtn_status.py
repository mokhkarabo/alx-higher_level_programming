#!/usr/bin/python3

"""
This script fetches the status of https://alx-intranet.hbtn.io/status using the requests package.
It displays the body of the response with tabulation before each line.
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

print("- Body response:")
for line in response.text.split('\n'):
    print("\t- " + line)
