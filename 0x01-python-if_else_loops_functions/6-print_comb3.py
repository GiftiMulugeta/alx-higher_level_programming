#!/usr/bin/python3
for i in range(0, 10):
    for j in (0, 10):
        if (i == j):
            continue
        else:
            print("{0}{1}".format(i,j))
