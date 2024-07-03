#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data: list[int]) -> bool:
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if 0 <= byte <= 127:
                # 1-byte character
                continue
            elif 192 <= byte <= 223:
                # 2-byte character
                num_bytes = 1
            elif 224 <= byte <= 239:
                # 3-byte character
                num_bytes = 2
            elif 240 <= byte <= 247:
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            if 128 <= byte <= 191:
                # Valid continuation byte
                num_bytes -= 1
            else:
                # Invalid continuation byte
                return False

    return num_bytes == 0


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
