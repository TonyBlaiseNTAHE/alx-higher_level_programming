#!/usr/bin/python3
"""
4-hbtn_status module
"""

from requests import get


if __name__ == '__main__':
        content = get('https://alx-intranet.hbtn.io/status')
        print('Body response:')
        print('\t- type: {}'.format(type(content.text.__class__)))
        print('\t- content: {}'.format(content.text))
