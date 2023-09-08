#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    s = "s"
    if n < 2:
        print("{:d} arguments.".format(n - 1))
    else:
        n = len(sys.argv) - 1
        if n == 1:
            print("{:d} argument:".format(n))
        else:
            print("{:d} argument{:s}:".format(n, s))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{:d}: {:s}".format(i, arg))
