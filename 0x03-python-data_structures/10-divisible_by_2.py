#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list1 = []
    list1 = [my_list[i] % 2 == 0 for i in range(len(my_list))]
    """
    for i in my_list:
        if my_list[i] % 2 == 0:
            list1.append(True)
        elif my_list[i] % 2 != 0:
            list1.append(False)
    """
    return (list1)
