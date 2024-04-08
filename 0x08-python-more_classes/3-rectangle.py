#!/usr/bin/python3
"""
This is the "0-rectangle" module.

The 0-rectangle module supplies one function, rectangle().
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value for the width regarding some restrictions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """serve as a getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value for the height regarding some conditions"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """prints the shape of the rectangle"""
        rect = ""
        if self.height == 0 or self.width == 0:
            return ""
        for _ in range(self.height):
            for _ in range(self.width):
                rect += "#" + "\n"
        return rect - "\n"
