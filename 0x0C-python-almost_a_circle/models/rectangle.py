#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base
"""Class Base"""


class Rectangle(Base):
    """Rectangle subclass"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instance attributes
        Args:
            width (int): width
            height (int): height
            x (int) = x
            y (int) = y
            id (int) = id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle to find
        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle instance to stdout with the char #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string to be printed
        Returns:
            print string
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates args to each attribute
        Args:
            args (int): args to send a non-keywords variable
                length argument list to a function
            kwargs (dict): length of args variables keywords
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """Creates a dictionary rep of a Rectangle
        Returns:
            Representation dictionary of a rectangle
        """
        a_dict = {"id": 0, "width": 0, "height": 0, "x": 0, "y": 0}
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "width":
                a_dict[key] = self.width
            elif key == "height":
                a_dict[key] = self.height
            elif key == "x":
                a_dict[key] = self.x
            elif key == "y":
                a_dict[key] = self.y
        return a_dict
