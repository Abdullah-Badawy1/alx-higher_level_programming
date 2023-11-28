#!/usr/bin/python3
"""Defines a function for printing a square using the # character."""


def print_square(size):
    """Print a square made of # characters.

    Args:
        size (int): The height/width of the square.
            It represents the number of rows and columns in the square.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Prints a square of '#' characters with the specified size.
    Each side of the square will have a length equal to 'size'.
    
    Example:
        >>> print_square(3)
        ###
        ###
        ###
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
