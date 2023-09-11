#!/usr/bin/python3
def no_c(my_string):
    s = ''.join([ch for ch in my_string if ch != 'c' and ch != 'C'])
    return s
