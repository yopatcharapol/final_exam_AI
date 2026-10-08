import copy

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    # Get the coordinates of empty cells
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, alpha, beta, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'O'
            eval = minimax(board_copy, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'X'
            eval = minimax(board_copy, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    alpha = float('-inf')
    beta = float('inf')

    for i, j in get_empty_cells(board):
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = 'O'
        move_val = minimax(board_copy, 0, alpha, beta, False)

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

        alpha = max(alpha, best_val)

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe Board:")
    print_board(board)

    for _ in range(9):  # Maximum of 9 moves
        if _ % 2 == 0:
            # Player 'X' move
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                _ -= 1  # Retry the same turn
            else:
                board[row][col] = 'X'
        else:
            # AI 'O' move
            print("AI 'O' is thinking...")
            row, col = find_best_move(board)
            board[row][col] = 'O'

        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You won!")
            break
        elif is_winner(board, 'O'):
            print("AI 'O' wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
