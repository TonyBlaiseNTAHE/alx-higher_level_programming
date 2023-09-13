#!/usr/bin/python3
def common_elements(set_1, set_2):
    for elem in set_1:
        for elemt in set_2:
            if elem == elemt:
                res = elem
    return res
