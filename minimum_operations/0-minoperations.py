#!/usr/bin/python3
"""
Minimum Operation"""

def minOperations(n):
    """Return 0 if n is less than or equal to 0"""
    
    if n <= 0:
        return 0
    operations = 0 
    for x in range(2, n/2):
        while(n % x == 0):
            operations += t 
            n = n / t
    return(operations)
