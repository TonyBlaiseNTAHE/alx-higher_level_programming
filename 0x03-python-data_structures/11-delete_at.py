#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        new_list = my_list
        if idx < 0:
            return new_list
        else:
            del new_list[idx]
            return new_list
    else:
        return None
