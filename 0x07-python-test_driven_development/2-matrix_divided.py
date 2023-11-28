#!/usr/bin/python3
"""
This module provides a function for printing a person's name.
It validates the input and formats the output according to given first and
last names.
"""


def display_full_name(given_name, surname=""):
    """
    Prints a full name in the format "My name is <given_name> <surname>".

    Args:
        given_name (str): The first name.
        surname (str): The last name. Optional.

    Raises:
        TypeError: If either given_name or surname is not a string.
    """
    # Validate that both given_name and surname are strings
    if not isinstance(given_name, str):
        raise TypeError('given_name must be a string')
    if not isinstance(surname, str):
        raise TypeError('surname must be a string')

    # Construct and print the full name
    full_name = "My name is " + given_name
    if surname:
        full_name += " " + surname
    print(full_name)
