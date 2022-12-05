#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = tuple_a + (0, 0)
    elif len(tuple_b) == 0:
        tuple_b = tuple_b + (0, 0)
    elif len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)
    elif len(tuple_a) > 2 and len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    summation = tuple(map(sum, zip(tuple_b, tuple_a)))
    return summation