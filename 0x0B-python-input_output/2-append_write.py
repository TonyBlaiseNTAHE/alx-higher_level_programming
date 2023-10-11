#!/usr/bin/python3
"""module containing a function called
append_write that appends a text to a file
"""


def append_write(filename="", text=""):
    """append function that appends texts
    to a file
       args: filename  - the file name
             text - the text to append to it
    """
    with open(filename, "+a", encoding="utf-8") as file:
        count = file.write(text)
        return count
