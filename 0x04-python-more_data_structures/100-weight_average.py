#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_weight = 0
        weighted_sum = 0
        for tup in my_list:
            value, weight = tup
            weighted_sum += value * weight
            total_weight += weight
        if total_weight != 0:
            weighted_average = weighted_sum / total_weight
            return weighted_average
        else:
            return 0
    else:
        return 0
