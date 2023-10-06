#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def calc():
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    oper = ["+", "-", "*", "/"]

    if argv[2] not in oper:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))

    if argv[2] == '-':
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))

    if argv[2] == '*':
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    if argv[2] == '/':
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))


if __name__ == "__main__":
    calc()
