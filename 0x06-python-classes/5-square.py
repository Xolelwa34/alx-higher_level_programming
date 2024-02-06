#!/usr/bin/python3
class Square:
    """Class square"""

    def __init__(self, size=0):
        """defines a square init"""
        self.size = size

    @property
    def size(self):
        """method to size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the square area"""
        return (self.__size**2)

    def my_print(self):
        """print to stdout square"""
        if self.__size is 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print('{}'.format('#'), end="")
            print()
