#!/usr/bin/python3
"""
defining a function called write_file
that write text into a file and return the
number of character readed
"""


def write_file(filename="", text=""):
    """write_file func
        args: filename - the file's name
             text - the text to right into
             the file
        returns: the length of the text written to the file       
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            length = len(text)
        return length
    except Exception as err:
        print("Error:", err)
        return 0
