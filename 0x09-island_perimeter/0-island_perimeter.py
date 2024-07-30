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
    m = len(grid[0])
    count = 0

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1:
                # check above
                if row == 0 or grid[row - 1][col] == 0:
                    count += 1
                # check below
                if row == n - 1 or grid[row + 1][col] == 0:
                    count += 1
                # check left
                if col == 0 or grid[row][col - 1] == 0:
                    count += 1
                # check right
                if col == m - 1 or grid[row][col + 1] == 0:
                    count += 1
    return count
