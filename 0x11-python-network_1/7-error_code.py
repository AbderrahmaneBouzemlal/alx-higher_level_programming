#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


if __name__ == '__main__':
	bad = requests.get(sys.argv[1])
	try:
		bad.raise_for_status()
		print(bad.text)
	except requests.exceptions.HTTPError:
		print(f"Error code: {bad.status_code}")

