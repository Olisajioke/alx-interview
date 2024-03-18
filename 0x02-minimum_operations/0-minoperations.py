#!/usr/bin/python3
""" Module for min_operations"""


def min_operations(n):
    """
    Calculates the minimum number of operations 
    needed to obtain exactly n H characters.
    """
    if n < 2:
        return 0
    ops = 0
    for base in range(2, n + 1):
        while n % base == 0:
            ops += base
            n //= base
    return ops
