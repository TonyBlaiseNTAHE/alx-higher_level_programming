#!/usr/bin/python3
"""
4-hbtn_status module
"""

from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read().decode('utf')
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content.strip()))
