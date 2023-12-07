#!/usr/bin/python3
def roman_to_int(roman_string):
    count = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    thon = 0
    y = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if count[roman_string[c]] >= y:
                thon += count[roman_string[c]]
            else:
                thon -= count[roman_string[c]]
            y = count[roman_string[c]]
    return thon
