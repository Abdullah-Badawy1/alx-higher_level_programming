#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        i = 1
        while i != (len(my_list) + 1):
            print("{:d}".format(my_list[-i]))
            i += 1
