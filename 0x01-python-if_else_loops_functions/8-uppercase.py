#!/usr/bin/python3
def uppercase(str):
    res = ""
    for element in str:
        if 'a' <= element <= 'z':
            res += chr(ord(element) - 32)
        else:
            res += element
    print(f"{res}")
