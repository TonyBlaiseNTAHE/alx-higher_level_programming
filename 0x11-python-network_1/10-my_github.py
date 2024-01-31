#!/usr/bin/python3
"""
takes github credentials and display your id
"""
import sys
from requests import get


if __name__ == '__main__':
    req = get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
