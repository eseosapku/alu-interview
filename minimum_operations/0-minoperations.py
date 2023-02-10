#!/usr/bin/python3
"""
Minimum Operation"""
def minOperations(n):
    """get minimum double , and one
    operations
    """


    operations = 0
    characters = 2
    while n > 1:
        while n % characters == 0:
            operations += characters
            n = n / characters
        characters += 1
    return operations
