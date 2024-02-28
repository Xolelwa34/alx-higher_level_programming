#!/usr/bin/python3
"""Defines Rectangle Class."""
from models.base import Base


class Rectangle(Base):
     """Class Rectangle that inherits from Base."""
    

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor."""
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
       """Get Width."""
        
        return self.__width

    @width.setter
    def width(self, value):
       """ Width setter."""
        
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
       """Get height."""
        
        return self.__height

    @height.setter
    def height(self, value):
       """ height setter."""
        
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
       """x getter."""
        
        return self.__x

    @x.setter
    def x(self, value):
       """ x setter."""
        
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
       """ y getter."""
        
        return self.__y

    @y.setter
    def y(self, value):
       """ y setter."""
        
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area."""
        
        return self.width * self.height

    def display(self):
       """ Prints Rectangle to
        console with #
        """
        for col in range(self.y):
            print()
        for y_axis in range(self.height):
            for x_axis in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Updates variadic args."""
        
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Dictionary representation."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width}

    def __str__(self):
       """ String representation"""
        
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))
