def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10

        # Check columns
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 10
            elif board[0][i] == 'O':
                return -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0  # If no winner yet

def minimax(board, depth, is_maximizing):
    # Check for terminal states (win, lose, draw) and evaluate the board
    score = evaluate(board)

    if score == 10:  # X wins
        return score - depth
    elif score == -10:  # O wins
        return score + depth
    elif not any('-' in row for row in board):  # Draw
        return 0

    if is_maximizing:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = '-'
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = '-'
        return best

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '-'

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

board = [['-','-','-'],['-','-','-'],['-','-','-']]
find_best_move(board)