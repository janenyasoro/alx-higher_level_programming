#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        first = None
    else:
        first = sentence[0]
    tuple_a = (leng, first)
    return (tuple_a)
