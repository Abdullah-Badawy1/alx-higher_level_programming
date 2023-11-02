#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    items = dir(hidden_4)
    index = 0

    while index < len(items):
        item = items[index]
        if item[0:2] != "__":
            print("{:s}".format(item))
        index += 1
