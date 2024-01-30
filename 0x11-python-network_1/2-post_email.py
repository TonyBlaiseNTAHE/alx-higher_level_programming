#!/usr/bin/python3
"""
2-post_email module
"""

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    email = sys.argv[2]

    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('ascii')
    
    req = urllib.request.Request(url=sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode())
