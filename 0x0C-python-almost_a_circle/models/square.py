#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle
"""Rectangle class"""


class Square(Rectangle):
    """Square class method"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes instance attributes
        Args:
            size (int): size
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """Method for string
        Returns:
            A string
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get size
        Returns:
            size return
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        Args:
            value (int): size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes
        Args:
            args (int): args update method
                
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Represents dictionary
        Returns:
            returns dictionary with attributes
        """
        my_dict = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in a_dict:
            if key == "id":
                my_dict[key] = self.id
            elif key == "size":
                my_dict[key] = self.width
                my_dict[key] = self.height
            elif key == "x":
                my_dict[key] = self.x
            elif key == "y":
                my_dict[key] = self.y
        return my_dict
