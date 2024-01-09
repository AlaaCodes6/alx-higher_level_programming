#!/usr/bin/python3
"""subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square subclass"""

    def __init__(self, size):
        """new square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        A function that finds the area of the Square
        """
        return self.__size ** 2

    def __str__(self):
        """
        a funtion to print square description

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
