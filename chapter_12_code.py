
# Chapter 12 Python Code - Backtracking (N-Queens Problem)
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

n_queens(4)  # Output: Solution for 4 queens
