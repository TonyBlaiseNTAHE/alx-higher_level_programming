#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError as a:
        sys.stderr.write("Exception: {}".format(a), file=sys.stderr)
        return False
    except TypeError as a:
        sys.stderr.write("Exception: {}".format(a), file=sys.stderr)
        return False
    
    
