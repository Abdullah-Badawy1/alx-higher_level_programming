#!/usr/bin/python3
"""Module 1-rectangle for Holberton Python project 0x08 task 1.

This module defines a Rectangle class. The Rectangle class, at this stage,
is designed to initialize a rectangle object with private width and height
attributes. It includes property setters and getters to manage these attributes,
ensuring that they adhere to specific type and value constraints.

"""

class Rectangle:
    """A class that defines a rectangle.

    This class represents a rectangle with width and height attributes.
    It includes mechanisms to set and retrieve these attributes while
    ensuring they are of appropriate type and value.

    Attributes:
        __width (int): The width of the rectangle, initialized to 0.
        __height (int): The height of the rectangle, initialized to 0.

    Args:
        width (int, optional): The initial width of the rectangle. Defaults to 0.
        height (int, optional): The initial height of the rectangle. Defaults to 0.

    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        The initialization involves setting the width and height of the rectangle.
        The property setters are used to apply the necessary validations.

        Args:
            width (int): The initial width of the rectangle.
            height (int): The initial height of the rectangle.

        """
        self.width = width  # Set width using the width property setter
        self.height = height  # Set height using the height property setter

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        The setter validates that the width is an integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Ensures that the width adheres to the type and value constraints.

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

        The setter validates that the height is an integer and not less than 0.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Ensures that the height adheres to the type and value constraints.

        Args:
            value (int): The height of the rectangle.

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
