#!/usr/bin/python3
def element_at(ret_list, idx):
    if idx >= len(ret_list) or idx < 0:
        return None
    return ret_list[idx]
