#!/usr/bin/python3
"""
send a post request to an URL with a letter
"""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    try:
        result = response.json()
        if result == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except ValueError:
        print('Not a valid JSON')
