#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            if i == x + 1:
                break
            print(f"{i}", end="")
        print()
        if x > i:
            return i
        else:
            return x
    except ValueError:
        print("Invalid element from the list")
