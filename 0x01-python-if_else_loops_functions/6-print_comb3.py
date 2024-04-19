#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for ret in range(0, 10):
    for ret1 in range(ret + 1, 10):
        if ret == 8 and ret1 == 9:
            print("{}{}".format(ret, ret1))
        else:
            print("{}{}".format(ret, ret1), end=", ")
