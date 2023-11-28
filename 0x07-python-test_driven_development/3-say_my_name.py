#!/usr/bin/python3
"""Defines a function for printing a person's name."""


def say_my_name(first_name, last_name=""):
    """Print a person's name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional):
        The last name of the person. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Prints the name in the format "My name is <first_name> <last_name>".
    If no last_name is provided, it prints only the first_name.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Alice")
        My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
