#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    summ = 0
    for i in my_list:
        mul = mul + (i[0] * i[1])
        summ = summ + i[1]
    total = mul / summ
    return total
