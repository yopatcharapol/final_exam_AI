count = 0

def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    global count
    if col == len(board):
        # All queens are placed, solution found
        print_board(board)
        count = count + 1 
        return True
    
    res = False

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place queen and move to the next column
            board[i][col] = 1

            # Recur to place the rest of the queens
            res = solve_n_queens_util(board, col + 1) or res

            # If placing queen in the current position doesn't lead to a solution, backtrack
            board[i][col] = 0
    
    return res

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")

def print_board(board):
    
    print("Num answer = ", count)

    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
    print()

# Example usage for 8-queen problem
solve_n_queens(8)