#!/usr/bin/python3
"""
0-htn_status module
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as content:
        data = content.read()

print('Body response:')
print('\t- type: {}'.format(type(data)))
print('\t- content: {}'.format(data))
print('\t- utf8 content: {}'.format(data.decode().strip()))
