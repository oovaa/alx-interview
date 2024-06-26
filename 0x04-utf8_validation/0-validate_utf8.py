#!/usr/bin/env python3

'''
0x04-utf8_validation task
'''

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines whether a given list of integers represents a valid UTF-8
    encoding.

    Args:
        data (List[int]): The list of integers representing the UTF-8 encoding.

    Returns:
        bool: True if the encoding is valid, False otherwise.
    """

    count = 0                                   # Keep a tally of non-first
    # bytes required

    for byte in data:                           # Pad out bytes to nine digits
        # and ignore the 1st 1
        # Ex: 35 = 0b100101 --> 35|256 = 0b1_00100101
        byte |= 256

        # Check for bad bytes.
        if (byte >> 3 == 0b1_11111 or               # One of first five digits
            # must be a 1
                (byte >> 6 == 0b1_10) ^ (count > 0)):       # Non-first byte
            # can happen if and only if the current count !=0.
            return False
            # Update counts after new byte. (1-byte -> no change
            # to count required because count == 0.)
        if byte >> 5 == 0b1_110:
            count = 1       # 2-byte first byte
        elif byte >> 4 == 0b1_1110:
            count = 2       # 3-byte first byte
        elif byte >> 4 == 0b1_1111:
            count = 3       # 4-byte first byte
        elif byte >> 6 == 0b1_10:
            count -= 1       # non-first bytes

    return not count
