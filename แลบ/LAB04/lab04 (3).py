import copy
import random
import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
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
    return [(i, j) for i in range(3) 
            for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
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
            
            eval = minimax(board_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = 'X'
            eval = minimax(board_copy, depth + 1, True)
            
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = 'O'
        # find maximize AI turn first
        if is_winner(board_copy, 'O'):
            return (i, j)
        move_val = minimax(board_copy, 0, False)

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def end_game(board):
    if is_winner(board, 'X'):
        print("Congratulations! You won!")
        return True
    elif is_winner(board, 'O'):
        print("AI 'O' wins! Better luck next time.")
        return True
    elif is_full(board):
        print("It's a draw!")
        return True

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    s = 0
    while True:
        if s == 9:
            break
        
        if s % 2 == 0:
            row, col = map(int, input("Enter your move (row space column): ").split())
            
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                s -= 1  # Retry the same turn
            else:
                board[row][col] = 'X'
        else:
            if s == 0:
                row, col = random.randint(0, 2), random.randint(0, 2)
                board[row][col] = 'O'
            else:
                # AI 'O' move
                print("AI 'O' is thinking...")
                row, col = find_best_move(board)
                board[row][col] = 'O'

        print_board(board)

        if end_game(board):
            break
        
        s += 1

if __name__ == "__main__":
    play_tic_tac_toe()
