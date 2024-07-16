#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the matrix in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        # After rotation, matrix will be:
        # [[7, 4, 1],
        #  [8, 5, 2],
        #  [9, 6, 3]]
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save top left
            top_left = matrix[top + i][l]

            # move bottom left to top left
            matrix[top + i][l] = matrix[bottom - i][l]

            # move bottom righ to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            matrix[top + i][r] = top_left

        l += 1
        r -= 1
