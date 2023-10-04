#!/usr/bin/python3
"""
function that prints a text with 2 new lines
args: text - the text to print
"""


def text_indentation(text):
    """if statement"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '.' or i == '?' or i == ':':
                print("{:s}".format(i))
                print()
                flag = 0
            else:
                print("{:s}".format(i), end="")
