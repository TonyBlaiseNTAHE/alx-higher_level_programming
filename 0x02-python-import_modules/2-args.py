#!/usr/bin/python3
import sys
n = len(sys.argv)
s = "s"
if n < 2:
    print("{:d} arguments.".format(n - 1))
else:
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("{:d} argument:".format(num_args))
    else:
        print("{:d} argument{:s}:".format(num_args, s))
    for i, arg in enumerate(sys.argv[1:], 1):
        print("{:d}: {:s}".format(i, arg))
