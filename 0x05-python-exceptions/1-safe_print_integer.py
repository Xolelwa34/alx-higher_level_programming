#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
    except Exception as e:
        return False
    else:
        return True
