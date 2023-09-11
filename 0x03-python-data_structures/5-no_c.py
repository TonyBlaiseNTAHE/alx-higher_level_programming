#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str = ""
        for ch in my_string:
            if ch != 'c' and ch != 'C':
                str += ch
        return str
