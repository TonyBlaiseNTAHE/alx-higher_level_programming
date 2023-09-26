#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as a:
        sys.stderr.write("Exception: {}\n".format(a))
        return False
    except TypeError as b:
        sys.stderr.write("Exception: {}\n".format(b))
        return False
