#!/usr/bin/python3
"""
This script takes in a URL,
Sends a request to the URL and
Displays the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request as req
import sys

if __name__ == '__main__':
	with req.urlopen(sys.argv[1]) as response:
		data = response.headers
		for k, v in data.items():
			if k == 'X-Request-Id':
				print(v)
