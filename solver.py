def isSafe(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num and i != col:
            return False

    for i in range(9):
        if sudoku[i][col] == num and i != row:
            return False
        
    rowBox = (row // 3) * 3
    colBox = (col // 3) * 3

    for r in range(rowBox, rowBox + 3):
        for c in range(colBox, colBox + 3):
            if sudoku[r][c] == num and (r, c) != (row, col):
                return False
    
    return True

def solve(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for n in range(1, 10):
                    if isSafe(sudoku, row, col, n):
                        sudoku[row][col] = n
                        if solve(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

def isValidSudoku(board):
    for i in range(9):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            if board[i][j]!=0 and board[i][j] in row:
                return False
            row[board[i][j]] = 1 
            
            if board[j][i]!=0 and board[j][i] in column:
                return False
            column[board[j][i]] = 1
            
            rc = row_cube+j//3
            cc = column_cube + j%3

            if board[rc][cc] in block and board[rc][cc]!=0:
                return False
            block[board[rc][cc]] = 1
    return True

def solver(sudoku):
    if  isValidSudoku(sudoku):
        solve(sudoku)
        return sudoku
    else:
        return None
