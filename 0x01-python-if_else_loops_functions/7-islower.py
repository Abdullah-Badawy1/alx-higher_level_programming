#!/usr/bin/python3

"""
This fun uses to know the lower and upper char.

Args:
    c (char) : Character to test.
Returns:
    return string tells upper or lower case.
"""


def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
