#!/usr/bin/python3
''' island perimeter calculator module '''


def island_perimeter(grid):
    ''' calculates and returns the perimeter of an island '''

    no_of_rows = len(grid)
    no_of_columns = len(grid[0])

    perimeter = 0
    for row in range(no_of_rows):
        for col in range(no_of_columns):
            if grid[row][col]:
                upper = (not row) or grid[row - 1][col] == 0
                lowerside = (row + 1 >= no_of_rows) or grid[row + 1][col] == 0
                leftside = (not col) or grid[row][col - 1] == 0
                right = (col + 1 >= no_of_columns) or grid[row][col + 1] == 0
                perimeter += upper + lowerside + leftside + right
    return perimeter
