#!/usr/bin/python3
"""
0. Lockboxes
mandatory
You have n number of locked boxes in front of
you. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes and their
        corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return True

    keys = set()
    opened = {i: False for i in range(len(boxes))}
    opened[0] = True
    for key in boxes[0]:
        keys.add(key)

    def open_box(box_idx):
        if not (0 <= box_idx < len(boxes)) or opened[box_idx]:
            return
        for key in boxes[box_idx]:
            keys.add(key)
        opened[box_idx] = True

    while keys:
        key = keys.pop()
        open_box(key)

    return all(opened.values())


# if __name__ == '__main__':
#     boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#     print(canUnlockAll(boxes))
