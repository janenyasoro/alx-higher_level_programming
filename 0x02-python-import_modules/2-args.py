#!/usr/bin/python3
from sys import argv


def fx():
    if len(argv) == 1:
        print("0 arguments.")
        return
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(1, argv[1]))
        return
    for i in range(len(argv)):
        if i == 0:
            print("{} arguments:".format(len(argv) - 1))
        else:
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    fx()
