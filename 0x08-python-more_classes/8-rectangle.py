#!/usr/bin/python3
"""Module 8-rectangle for Holberton Python project 0x08 task 8.

This module defines a Rectangle class with comprehensive functionality including
methods to calculate area, perimeter, string representations (__str__, __repr__),
a custom deletion message (__del__), and a static method to compare the size of
two Rectangle instances.

"""

class Rectangle:
    """A class for representing a rectangle.

    This class includes comprehensive functionalities such as calculating area
    and perimeter, customizable string representations, tracking the number of
    instances, and a method to compare the sizes of two Rectangle instances.

    Class Attributes:
        number_of_instances (int): The count of Rectangle instances.
        print_symbol (Any): The symbol used for the string representation of
            the rectangle. Can be any type.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.

    """

    number_of_instances = 0  # Class-level attribute for tracking instances
    print_symbol = '#'       # Default symbol for string representation

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Increments the `number_of_instances`. Sets width and height with
        property setters including type and value validations.

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

        Ensures the width is an integer and not less than 0.

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

        Ensures the height is an integer and not less than 0.

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
        """Creates a string representation of the rectangle using `print_symbol`.

        Forms a string using the `print_symbol` to depict the rectangle's shape.

        Returns:
            str: A string representation of the rectangle.

        """
        rectangle_str = ""
        for row in range(self.__height):
            rectangle_str += "{}".format(self.print_symbol) * self.__width
            if row < self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __str__(self):
        """Enables direct printing of Rectangle instances.

        Returns a string representation of the rectangle for printing.

        Returns:
            str: The output of _draw_rectangle, suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Provides a string representation of the Rectangle instance for eval().

        Returns a string of code that can recreate the current instance.

        Returns:
            str: A string of code that can recreate the rectangle instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message upon deletion of a Rectangle instance and decrements `number_of_instances`.

        Reduces the class-level instance counter and prints a custom message
        when an instance is deleted.

        """
        type(self).number_of_instances -= 1  # Decrement instance counter
        print('Bye rectangle...')  # Print the custom message

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines the larger of two Rectangle instances based on area.

        Compares the area of two Rectangle instances and returns the one with
        the larger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle instance.

        Returns:
            Rectangle: The rectangle with the larger or equal area.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
