#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
	letter = ""
	if sys.argv[1]:
		letter = sys.argv[1]

	res = requests.post(
		'http://0.0.0.0:5000/search_user',
		data={
		'q': letter
		}
		)
	if res.text == "":
		print("No result")
		return
	try:
		d = res.json()
		print("[{}] {}".format(d.get("id"), d.get("name")))
	except requests.exceptions.JSONDecodeError:
		print('Not a valid JSON')
