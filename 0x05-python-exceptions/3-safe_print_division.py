#!/usr/bin/python3
def safe_print_division(a, b):
    try:
    number = a / b
    except Exception as e:
        number = None
    finally:
        print("Inside result: {}".format(number))
    return number
