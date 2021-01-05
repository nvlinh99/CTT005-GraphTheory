import random

grid = [
	[5, 3, 0, 0, 7, 0, 0, 0, 0], 
	[6, 0, 0, 1, 9, 5, 0, 0, 0], 
	[0, 9, 8, 0, 0, 0, 0, 6, 0], 
	[8, 0, 0, 0, 6, 0, 0, 0, 3], 
	[4, 0, 0, 8, 0, 3, 0, 0, 1], 
	[7, 0, 0, 0, 2, 0, 0, 0, 6], 
	[0, 6, 0, 0, 0, 0, 2, 8, 0], 
	[0, 0, 0, 4, 1, 9, 0, 0, 5], 
	[0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def findNextCellToFill(sudokuGrid):
    for x in range(0, 9):
        for y in range(0, 9):
            if sudokuGrid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudokuGrid, i, j, e):
    rowOk = all([e != sudokuGrid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudokuGrid[x][j] for x in range(9)])
        if columnOk:
            TopX, TopY = 3 * (i//3), 3 * (j//3)
            for x in range(TopX, TopX + 3):
                for y in range(TopY, TopY + 3):
                    if sudokuGrid[x][y] == e:
                        return False
            return True
    return False

def solveSudoku(sudokuGrid, i=0, j=0):
    i, j = findNextCellToFill(sudokuGrid)
    if i == -1:
        return True
    for p in range(1, 10):
        e = random.randrange(1, 10)
        if isValid(sudokuGrid, i, j, e):
            sudokuGrid[i][j] = e
            if solveSudoku(sudokuGrid, i, j):
                return True
            # Undo the current cell for backtracking
            sudokuGrid[i][j] = 0
    return False

solveSudoku(grid, 0, 0)
for i in range(9):
		for value in grid[i]:
				print(value, end=" ")
		print()