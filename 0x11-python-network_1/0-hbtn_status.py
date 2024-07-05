#!/usr/bin/python3
"""
This module contain a script that fetches to an url
"""
import urllib.request as req


if __name__ == '__main__':
    """processing the response """
    reque = req.Request('https://alx-intranet.hbtn.io/status')
    with req.urlopen(reque) as response:
        data = response.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {data.decode("utf-8")}')
