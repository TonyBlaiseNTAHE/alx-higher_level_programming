#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        n = len(my_list)
        new_list = [False] * n
        for i in range(n):
            if my_list[i] % 2 == 0:
                new_list[i] = True
        return new_list
