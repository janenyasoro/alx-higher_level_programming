#!/usr/bin/python3


def no_c(my_string):
    str0 = ""
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            str0 = str0 + my_string[i]
    return (str0)
