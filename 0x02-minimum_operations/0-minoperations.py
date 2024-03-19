#!/usr/bin/python3
""" Module for min_operations"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    needed to obtain exactly n H characters.
    """
    if n < 2:
        return 0
    op = 0
    for base in range(2, n + 1):
        while n % base == 0:
            op += base
            n //= base
    return op
