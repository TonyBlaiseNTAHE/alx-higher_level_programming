#!/usr/bin/python3
def search_replace(my_list, search, replace):
    j = len(my_list)
    new_list = [0 for _ in range(j)]
    for i in range(j):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
    return new_list
