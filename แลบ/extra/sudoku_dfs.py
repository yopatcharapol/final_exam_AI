import time


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def is_valid(board, row, col, num):
    # Check exist at 9 rows or 9 columns
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check exist in 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    empty_location = find_empty_location(board)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


if __name__ == "__main__":
    sudoku_board = [
        [7, 0, 9, 4, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 0],
        [8, 0, 4, 2, 0, 0, 0, 0, 9],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [6, 0, 7, 0, 5, 0, 9, 0, 0],
    ]

    print("Problem:")
    print_board(sudoku_board)

    avg = 0
    for i in range(10):
        start = time.time()

        if solve_sudoku(sudoku_board):
            print("\nSolution:")
            print_board(sudoku_board)
        else:
            print("\nNo solution exists.")

        compute = time.time() - start
        print(f"computed time: %.2f" % compute)

        avg += compute

    print(f"average computed time: %.2f" % (avg / 10))


