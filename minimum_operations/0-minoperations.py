#!/usr/bin/python3
"""Minimum Operation"""


def minOperations(n):
    """get minimum double , and one
    operations
    """
    x = 0
    char = 2
    while n > 1:
        while n % char == 0:
            x += char
            n = n / char
        char += 1
    return x
