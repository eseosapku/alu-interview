#!/usr/bin/python3
"""
comment
"""


def pascal_triangle(n):
    """
    comment
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for number in range(n-1):
        pascal.append(
            [a+b for a, b in zip([0] + pascal[-1], pascal[-1] + [0])])

    return pascalpp.run(host="0.0.0.0", port=5000, debug=True)
