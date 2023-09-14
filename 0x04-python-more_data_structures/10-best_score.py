#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        Max = 0
        best_key = None
        for key, value in a_dictionary.items():
            if value > Max:
                Max = value
                best_key = key
        return best_key
