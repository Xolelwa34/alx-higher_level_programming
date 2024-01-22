#!/usr/bin/python3
def print_reversed_list_integer(ret_list=[]):
    if ret_list:
        if len(ret_list) > 0:
            l = len(ret_list) - 1
            for i in ret_list:
                print('{}'.format(ret_list[l]))
                l -= 1
