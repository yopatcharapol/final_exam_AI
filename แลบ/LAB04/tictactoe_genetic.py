# incompleted code
import random

def initialize_board():
    return [' '] * 9

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n")
    print('\n')

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def make_move(board, move, player):
    board[move] = player

def opponent_move(board, player):
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)

def evaluate_board(board):
    if is_winner(board, 'X'):
        return 1  # Agent wins
    elif is_winner(board, 'O'):
        return -1  # Opponent wins
    elif is_board_full(board):
        return 0  # Draw
    else:
        return 2  # Game still ongoing

def generate_individual():
    return [random.randint(0, 8) for _ in range(9)]

def fitness(individual):
    board = initialize_board()
    for move in individual:
        make_move(board, move, 'X')
        if evaluate_board(board) != 2:
            break
        opponent_move(board, 'O')
        if evaluate_board(board) != 2:
            break
    return evaluate_board(board)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual):
    mutation_point = random.randint(0, len(individual) - 1)
    individual[mutation_point] = random.randint(0, 8)
    return individual

def play_tic_tac_toe():
    population_size = 20
    generations = 100

    population = [generate_individual() for _ in range(population_size)]

    for generation in range(generations):
        fitness_scores = [(individual, fitness(individual)) for individual in population]

        fitness_scores.sort(key=lambda x: x[1])

        best_individual = fitness_scores[0][0]
        print(f"Generation {generation + 1} - Best Moves: {best_individual}, Fitness: {fitness_scores[0][1]}")

        if fitness_scores[0][1] == 1:
            print("Agent wins!")
            break

        parents = [individual for individual, _ in fitness_scores[:int(0.2 * population_size)]]

        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            child = mutate(crossover(parent1, parent2))
            offspring.append(child)

        population = parents + offspring

    print("Final Board:")
    board = initialize_board()
    for move in best_individual:
        make_move(board, move, 'X')
        display_board(board)
        if evaluate_board(board) != 2:
            break
        opponent_move(board, 'O')
        display_board(board)
        if evaluate_board(board)  != 2:
            break

if __name__ == "__main__":
    play_tic_tac_toe()