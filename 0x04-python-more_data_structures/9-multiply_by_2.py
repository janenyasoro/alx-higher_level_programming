#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for k, v in new_dictionary.items():
        v = v * 2
        new_dictionary[k] = v
    return (new_dictionary)
