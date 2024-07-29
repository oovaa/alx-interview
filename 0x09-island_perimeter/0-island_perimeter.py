#!/usr/bin/python3

"""
    Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    n = len(grid)
    count = 0

    for row in range(n):
        for col in range(n):
            if grid[row][col]:

                # check above and below
                if row > 0 and grid[row - 1][col] == 0:
                    count += 1
                if row < n and grid[row + 1][col] == 0:
                    count += 1
                # check sides
                if col > 0 and grid[row][col - 1] == 0:
                    count += 1
                if col < n and grid[row][col + 1] == 0:
                    count += 1
    return count
