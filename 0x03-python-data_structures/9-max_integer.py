#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if my_list:
        for i in my_list[1:]:
            if i > max_value:
                max_value = i
        return int(max_value)
    else:
        return None
