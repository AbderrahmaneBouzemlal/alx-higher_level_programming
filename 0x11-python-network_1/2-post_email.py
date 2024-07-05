#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request as req
import sys

if __name__ == '__main__':
    email = sys.argv[2].encode('ascii')
    request = req.Request(sys.argv[1], data=email)
    with req.urlopen(request) as response:
        data = response.read()
        print(data.decode('utf-8'))
