#!/usr/bin/python3

d = {'Mike': 40, 'John': 25, 'Jimmy': 30, 'Tony': 30}
max_v = 0 
for  key, value  in d.items():
    if value > max_v:
        max_v = value
print("Best score: {}".format(max_v))
