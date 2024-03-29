#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count >= x:
                break
            print("{}".format(i), end="")
            count += 1
        print()
        return count
    except ValueError:
        print("Invalid element from the list")
