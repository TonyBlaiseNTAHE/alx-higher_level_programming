#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 6, 7, 29, 89]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
