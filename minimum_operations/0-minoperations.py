#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    x = 2
    while x <= n:
        while n % x == 0:
            operations += i
            n /= x
        x += 1

    if operations == 0:
        return n

    return operations
