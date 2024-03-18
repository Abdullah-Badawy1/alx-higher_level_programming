#!/usr/bin/python3
for x in range(122, 96, -1):
    print(f'{chr(x).upper() if (x % 2) != 0 else chr(x)}', end='')
