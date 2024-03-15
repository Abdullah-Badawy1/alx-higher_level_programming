#!/usr/bin/python3
"""
The uppercase function convert from lower to upper.

Args:
    str (string) :the string which should be converted.

Return:
    return string after convertion.
"""


def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            char = chr(ord(c)).upper()
        else:
            char = c
        print(f"{char}", end="")
    print('')
