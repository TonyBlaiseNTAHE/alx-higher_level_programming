#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = lambda x: x * number
    return list(map(new_list, my_list))
