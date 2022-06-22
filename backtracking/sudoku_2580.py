sudoku = []

sudoku_row = []

zero_List = []

for i in range(9):
    sudoku_row = list(map(int, input().split()))
    sudoku.append(sudoku_row)
    sudoku_row = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_List.append((i,j))


def row_check(point, col):
    for i in range(9):
        if sudoku[col][i] == point:
            return False
    return True

def col_check(point, row):
    for i in range(9):
        if sudoku[i][row] == point:
            return False
    return True

def box_check(point, col, row):
    x = col//3
    y = row//3

    for i in range(3):
        for j in range(3):
            if sudoku[x*3 + i][y*3 + j] == point:
                return False
    return True

def all_check(point, col, row):
    return row_check(point, col) and col_check(point, row) and box_check(point, col, row)

def print_sudoku():
    for i in range(9):
        print(*sudoku[i])

def dfs(idx):
    if idx == len(zero_List):

        print_sudoku()
        exit()

    for i in range(1,10):
        if all_check(i, zero_List[idx][0], zero_List[idx][1]):
            sudoku[zero_List[idx][0]][zero_List[idx][1]] = i
            dfs(idx+1)
            sudoku[zero_List[idx][0]][zero_List[idx][1]] = 0



dfs(0)
