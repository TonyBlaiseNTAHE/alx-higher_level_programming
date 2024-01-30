#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    import sys

    content = get(sys.argv[1])
    for head, value in content.headers.items():
        if head == 'X-Request-Id':
            print(f'{value}')
