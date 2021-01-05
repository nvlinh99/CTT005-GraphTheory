import random
import itertools as it

# Lấy một danh sách các số làm đầu vào và trả về một hoán vị theo các cách khác nhau mà chúng có thể được đặt


def getRandomPairs(numbers):
    l = len(numbers)
    # Tạo tất cả các cặp không lặp lại có thể có
    # it.permutations: Trả về các hoán vị độ dài r liên tiếp của các phần tử trong có thể lặp lại.
    listPairs = list(it.permutations(numbers, l))
    # Trộn ngẫu nhiên các cặp
    random.shuffle(listPairs)
    return listPairs

# Kiểm tra l1 phải được kiểm tra nếu nó có trong l2 không


def checkLists(l1, l2):
    l = len(l1)
    for i in l2:
        for j in range(l):
            if l1[j] == i[j]:
                return False  # Cùng index
    return True

# Funcs use for 9x9


def findNextCellToFill(sudokuGrid, n):
    for x in range(0, n):
        for y in range(0, n):
            if sudokuGrid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudokuGrid, i, j, e, n):
    rowOk = all([e != sudokuGrid[i][x] for x in range(n)])
    if rowOk:
        columnOk = all([e != sudokuGrid[x][j] for x in range(n)])
        if columnOk:
            TopX, TopY = 3 * (i//3), 3 * (j//3)
            for x in range(TopX, TopX + 3):
                for y in range(TopY, TopY + 3):
                    if sudokuGrid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudokuGrid, i=0, j=0, n=9):
    i, j = findNextCellToFill(sudokuGrid, n)
    if i == -1:
        return True
    for p in range(1, n + 1):
        e = random.randrange(1, n + 1)
        if isValid(sudokuGrid, i, j, e, n):
            sudokuGrid[i][j] = e
            if solveSudoku(sudokuGrid, i, j, n):
                return True
            # Undo the current cell for backtracking
            sudokuGrid[i][j] = 0
    return False


def main():
    n = int(input("Enter N: "))
    choice = getRandomPairs([x for x in range(1, n + 1)])
    choice = [list(ch) for ch in choice]
    sudoku = []
    sudoku.append(choice[0])
    for ch in choice:
        if checkLists(ch, sudoku):
            sudoku.append(ch)
        if len(sudoku) == n:
            break

    if len(sudoku) != 9:
        print()
        for _ in sudoku:
            for i in _:
                print(i, end=" ")
            print()
    else:
        newSudoku = []
        row = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                row.append(0)
            newSudoku.append(row)
        solveSudoku(newSudoku, 0, 0, n)
        print()
        for i in range(n):
            for value in newSudoku[i]:
                print(value, end=" ")
            print()


if __name__ == "__main__":
    main()
