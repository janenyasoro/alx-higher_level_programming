#!/usr/bin/python3
from sys import argv


def infinite_add():
    s = 0
    for i in range(1, len(argv)):
        s += (int(argv[i]))
    print(s)


if __name__ == "__main__":
    infinite_add()
