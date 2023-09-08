#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from decimal import Decimal
    n = len(sys.argv)
    j = Decimal(0)
    for i in range(1, n):
        try:
            j += Decimal(sys.argv[i])
        except ValueError:
            print("Error: Invalid input argument:", sys.argv[i])
print("{:s}".format(str(j)))
