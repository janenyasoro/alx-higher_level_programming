#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print("{}".format(chr(i)), end="")
