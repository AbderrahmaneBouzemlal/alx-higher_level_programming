#!/usr/bin/python3
"""In this module the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id == None:
            super(Rectangle, self).__init__(id)
        else:
            self.id = id

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def update(self, *args, **kwargs):
        length = len(args)

        if length > 0:
            for i in range(length):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def area(self):
        return self.width * self.height

    def display(self):
        rect =  "" + "\n" * self.y
        rect += "\n".join(" " * self.x + "#" * self.__width
                          for _ in range(self.__height))
        print(rect)

    def __str__(self):
        return f"[{Rectangle.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
