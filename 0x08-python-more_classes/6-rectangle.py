#!/usr/bin/python3
"""Module 6-rectangle for Holberton Python project 0x08 task 6.

This module defines a Rectangle class with additional functionality to keep
track of the number of instances. It also includes methods for area and
perimeter calculations, string representations (__str__, __repr__), and
a custom deletion message (__del__).

"""


class Rectangle:
    """A class for representing a rectangle.

    This class extends the Rectangle functionalities by maintaining a count of
    the number of instances created and deleted. It provides methods for
    calculating the area and perimeter,
    and mechanisms to represent the object
    as a string for printing or as a string of code
    that can recreate the object.

    Class Attributes:
        number_of_instances (int): The count of Rectangle instances.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.

    """

    number_of_instances = 0  # Class-level attribute for tracking instances

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Increments the `number_of_instances`. Sets the width and height of
        the rectangle using property setters with type and value validations.

        Args:
            width (int): The initial width of the rectangle.
            height (int): The initial height of the rectangle.

        """
        type(self).number_of_instances += 1  # Increment instance counter
        self.width = width  # Set width using the width property setter
        self.height = height  # Set height using the height property setter

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        Validates the width as an integer and ensures it's not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Validates the width as an integer and not less than 0.

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

        Validates the height as an integer and ensures it's not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Validates the height as an integer and not less than 0.

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
        """Creates a string representation of
        the rectangle using '#' characters.

        Forms a string of '#' characters depicting the rectangle's shape
        based on its dimensions.

        Returns:
            str: A string representation of the rectangle.

        """
        rectangle_str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rectangle_str += '#'
            if self.__width != 0 and row < self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __str__(self):
        """Enables direct printing of Rectangle instances.

        Uses _draw_rectangle to create
        a string representation of the rectangle.

        Returns:
            str: The output of _draw_rectangle, suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Provides a string representation of
        the Rectangle instance for eval().

        Returns a string of code that can recreate the current instance.

        Returns:
            str: A string of code that can recreate the rectangle instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrements `number_of_instances` and prints a
        message upon instance deletion.

        Reduces the class-level instance counter and prints a custom message
        when an instance is deleted.

        """
        cls.number_of_instances -= 1  # Decrement instance counter
        print('Bye rectangle...')  # Print the custom message
