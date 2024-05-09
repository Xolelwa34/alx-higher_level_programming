#!/usr/bin/python3
"""Script that's used to find peak in a list of integers
"""

"""
    In the process
        Since it's not sorted, the sorting will take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """Functionn that finds a peak in a list of unsorted integers
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
