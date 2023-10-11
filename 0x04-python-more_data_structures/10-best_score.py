#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = max(sorted(a_dictionary.values()))
        for i, v in a_dictionary.items():
            if a == v:
                return (i)
    else:
        return (None)
