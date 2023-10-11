#!/usr/bin/python3
"""
defining a function called read_file that
reads word from file and prints it to stdout
"""


def read_file(filename=""):
    """ read_file function
        agrs: filename - the name of the file
        to read from
    """
    with open(filename, encoding="utf-8") as file:
        f = file.read()

    for word in f:
        print(word, end="")
