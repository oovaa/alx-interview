#!/usr/bin/python3
"""
Main file for calculating minimum operations to reach n characters
starting from a single character "A"
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations to reach exactly n characters.

    Args:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations needed to reach n characters.
    """
    if n <= 1:
        return 0
    ops = 0
    while 1 < n:
        for i in range(2, n + 1):
            while n % i == 0:
                ops += i
                n //= i
                print(f"ops: {ops}, i: {i}, n: {n}\n")
    return ops
