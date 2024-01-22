#!/usr/bin/python3
def replace_in_list(ret_list, idx, element):
    if idx >= len(ret_list) or idx < 0:
        return ret_list
    ret_list[idx] = element
    return ret_list
