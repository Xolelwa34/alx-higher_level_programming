#!/usr/bin/python3
"""Defines a square"""

class Square:
    """square class"""

    def __init__(self, size=0):
        """method to initiate"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """square area"""
        return (self.__size**2)
