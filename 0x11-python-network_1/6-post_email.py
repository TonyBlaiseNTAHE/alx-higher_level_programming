#!/usr/bin/python3
"""
6-post_email module
"""

from requests import post
from sys import argv


if __name__ == '__main__':
    content = post(argv[1], data={'email': argv[2]})
    print(content.text)
