#!/usr/bin/python3
def no_c(my_string):
    new_user = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            new_user += i
    return new_user
