#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for i in my_list:
        if i not in unique:
            unique.append(i)
    for j in unique:
        total = total + j
    return total
