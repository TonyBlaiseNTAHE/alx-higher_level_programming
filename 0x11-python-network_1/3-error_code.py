#!/usr/bin/python3
"""
sends a request to the URL and display the body
of the response and handle Error code.
"""

import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
