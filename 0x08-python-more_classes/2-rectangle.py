#!/usr/bin/python3
"""Module 2-rectangle for Holberton Python project 0x08 task 2.

This module defines a Rectangle class with functionalities to calculate the
area and perimeter of a rectangle. It includes methods for setting and getting
the width and height with appropriate validations.

"""


class Rectangle:
    """A class representing a rectangle.

    This class provides functionalities for calculating the area and perimeter
    of a rectangle. It handles the initialization width and height attributes
    with appropriate type and value validations.

    Attributes:
        __width (int): The width of the rectangle, initialized to 0.
        __height (int): The height of the rectangle, initialized to 0.

    Args:
        width (int, optional): The initial width of the rectangle.
        height (int, optional):initial height of the rectangle. Defaults to 0.

    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        The initialization sets the width and height of the rectangle.
        Property setters are utilized for validations.

        Args:
            width (int): The initial width of the rectangle.
            height (int): The initial height of the rectangle.

        """
        self.width = width  # Set width using the width property setter
        self.height = height  # Set height using the height property setter

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        The setter validates that the width is integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Ensures that the width adheres to type and value constraints.

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

        The setter validates that the height
        is an integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Ensures that the height adheres to type and value constraints.

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

        The area is calculated as the product of the width and height.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        The perimeter is calculated as twice the sum of the width and height.
        Returns 0 if either width or height is 0.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
