#code adapted from https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
def main():
    #CHANGE BOARD VARIABLE TO TRY A DIFFERENT SUDOKU PROBLEM
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    print("____Intial Board____")

    for row in board:
        print(row)

    solve(board)

    print("____Finished Board____")

    for row in board:
        print(row)

#Backtracking alg
def solve(board: list) -> bool:
    for row in range(0,9):
        for column in range (0,9):
            if board[row][column] == ".":
                for i in range(1,10):
                    board[row][column] = str(i)
                    if verify(board, row, column):
                        if solve(board):
                            return True
                        else:
                            board[row][column] = "."
                    else:
                        board[row][column] = "."
                return False
    return True


#Checks if the number inserted is legal
def verify(board: list, row: int, column: int) ->bool:
    return (rowCheck(board,row) and colCheck(board,column) and boxCheck(board, row, column))

def rowCheck(board: list, rowNum: int) -> bool:
    row = board[rowNum]
    present = []
    for cell in row:
        if cell== ".":
            continue
        elif cell not in present:
            present.append(cell)
        else:
            return False
    return True

def colCheck(board: list, colNum: int) -> bool:
    present = []
    for row in board:
        if row[colNum]==".":
            continue
        elif row[colNum] not in present:
            present.append(row[colNum])
        else:
            return False
    return True

def boxCheck(board: list, row: int, col: int) -> bool:
    present = []
    rowBox = row/9*3
    colBox = col/9*3
    if rowBox > 2:
        rows = [6,9]
    elif rowBox <= 1:
        rows = [0,3]
    else:
        rows = [3,6]

    if colBox > 2:
        cols = [6,9]
    if colBox <= 1:
        cols = [0,3]
    else:
        cols = [3,6]
    for i in range(rows[0],rows[1]):
        for j in range(cols[0],cols[1]):
            if board[i][j] == ".":
                continue
            elif board[i][j] not in present:
                present.append(board[i][j])
            else:
                return False
    return True


if __name__ == '__main__':
    main()
