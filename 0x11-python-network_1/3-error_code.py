#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL and
displays the body of
the response (decoded in utf-8)
"""
import sys
import urllib.request as request
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        req = request.Request(sys.argv[1])
        with request.urlopen(req) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except HTTPError as error:
        print(f'Error code: {error.status}')
