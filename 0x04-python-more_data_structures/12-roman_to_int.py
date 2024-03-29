#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    romanN_set = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    current_value = 0
    prev_value = 0
    result = 0
    for c in roman_string[::-1]:
        current_value = romanN_set[c]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            prev_value = current_value
    if 1 <= result <= 3999:
        return result
    else:
        return 0
