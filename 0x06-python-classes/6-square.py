#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (int, int): The position to set for the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        i = 0
        while i < self.__position[1]:
            print("")
            i += 1

        i = 0
        while i < self.__size:
            j = 0
            while j < self.__position[0]:
                print(" ", end="")
                j += 1
            k = 0
            while k < self.__size:
                print("#", end="")
                k += 1
            print("")
            i += 1
