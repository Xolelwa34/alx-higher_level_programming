#!/usr/bin/python3
class Square:
    """Class Square"""

    def __init__(self, size=0):
        """method that initiates"""
        self.size = size

    @property
    def size(self):
        """ method to retrieve"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method that nitiate value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """method that returns the current square area"""
        return (self.__size**2)
