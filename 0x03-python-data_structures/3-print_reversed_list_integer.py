#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        if len(my_list) > 0:
            n = len(my_list) - 1
            for i in my_list:
                print('{}'.format(my_list[n]))
                n = 1
