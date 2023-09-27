#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as b:
        sys.stderr.write("Exception: {}".format(b))
        return False
    except ValueError as a:
        sys.stderr.write("Exception: {}".format(a))
        return False
