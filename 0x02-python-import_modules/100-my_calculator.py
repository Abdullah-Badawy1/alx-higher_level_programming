#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

ops = ['+', '-', '*', '/']
argc = len(argv)

if __name__ == '__main__':
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operator = argv[2]
    if operator not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a, b = int(argv[1]), int(argv[3]
    result = None
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print(f'{a} {operator} {b} = {result}')
