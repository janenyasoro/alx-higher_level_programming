#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_list = set(my_list)
    for i in my_list:
        result = result + i
    return (result)
