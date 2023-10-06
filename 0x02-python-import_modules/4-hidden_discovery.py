#!/usr/bin/python3
import hidden_4


def revealer():
    names = dir(hidden_4)
    for w in names:
        if not w.startswith("_"):
            print(w)


if __name__ == "__main__":
    revealer()
