#!/usr/bin/python3
"""Module 3-rectangle for Holberton Python project 0x08 task 3.

This module defines a Rectangle class with functionalities for calculating
area and perimeter, and includes a method to produce a string representation
of the rectangle.

"""


class Rectangle:
    """A class for representing a rectangle.

    This class provides the functionality to create a rectangle object with
    width and height attributes. It includes methods to calculate the area
    and perimeter of the rectangle and a special method to output a string
    representation of the rectangle using the `__str__` method.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.

    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        The initialization sets the width and height of the rectangle using
        property setters which include validations for type and value.

        Args:
            width (int): The initial width of the rectangle.
            height (int): The initial height of the rectangle.

        """
        self.width = width  # Set width using the width property setter
        self.height = height  # Set height using the height property setter

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        The setter ensures the width is an integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Validates that the width is an integer and not less than 0.

        Args:
            value (int): The width of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle.

        The setter ensures the height is an integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Validates that the height is an integer and not less than 0.

        Args:
            value (int): The height of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Computes the area as the product of width and height.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Computes the perimeter as twice the sum of width and height.
        Returns 0 if either width or height is 0.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Creates a string representation of the rectangle.

        Constructs a string of '#' characters that represents the rectangle's
        shape, using the dimensions of width and height.

        Returns:
            str: A string representation of the rectangle.

        """
        rectangle_str = ""
        row = 0
        while row < self.__height:
            col = 0
            while col < self.__width:
                rectangle_str += '#'
                col += 1
            if self.__width != 0 and row < self.__height - 1:
                rectangle_str += '\n'
            row += 1
        return rectangle_str

    def __str__(self):
        """Enables direct printing of Rectangle instances.

        Uses _draw_rectangle to create string representation of the rectangle

        Returns:
            str: The output of _draw_rectangle, suitable for printing.

        """
        return self._draw_rectangle()
