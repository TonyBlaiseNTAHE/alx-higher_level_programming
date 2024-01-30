#!/usr/bin/python3
"""
1-hbtn_header module
"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        for header, value in response.headers.items():
            if header == 'X-Request-Id':
                print('{}'.format(value))
