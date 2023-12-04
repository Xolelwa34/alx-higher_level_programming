#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    high = my_list[:]
    if idx >= 0 and idx < len(high):
        high[idx] = element
    return high
