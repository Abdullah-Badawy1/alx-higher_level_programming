#!/usr/bin/python3

# Write a function that divides 2 integers and prints the result

def safe_print_division(a, b):
    divide = None
    try:
        divide = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(divide))
        return divide
