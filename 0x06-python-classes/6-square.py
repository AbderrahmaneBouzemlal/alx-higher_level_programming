#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the square
            position(tuple): the coordinates of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the current square area."""
        if self.__size <= 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(' ', end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        for i in value:
            if not isinstance(i, int) \
                or isinstance(value, tuple)\
                or i < 0\
                    or len(value) != 0:
                raise TypeError("position must be a tuple of \
                                2 positive integers")
            self.__position = value

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
