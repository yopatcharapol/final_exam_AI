import random

# Tic-Tac-Toe board size
BOARD_SIZE = 3

# Number of individuals in the population
POPULATION_SIZE = 50

# Number of generations
NUM_GENERATIONS = 100

# Mutation rate
MUTATION_RATE = 0.1

def initialize_board():
    return [' '] * 9

# Function to initialize a random individual (Tic-Tac-Toe strategy)
def initialize_individual():
    return [random.choice(['X', 'O', '']) for _ in range(BOARD_SIZE * BOARD_SIZE)]

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to calculate the fitness of an individual
def calculate_fitness(individual, opponent_moves):
    # Simulate a game between the individual and the opponent (human)
    board = [[''] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    
    for i in range(BOARD_SIZE * BOARD_SIZE):
        if i % 2 == 0:
            # AI's move (even index)
            move = individual[i]
        else:
            # Opponent's move (odd index)
            move = opponent_moves[i // 2]

        import pdb
        pdb.set_trace()
        row, col = divmod(move, BOARD_SIZE)
        if board[row][col] == '':
            board[row][col] = 'X' if i % 2 == 0 else 'O'
        else:
            # Invalid move, penalize the fitness
            return -1

        if check_winner(board, 'X'):
            return 1  # AI wins
        elif check_winner(board, 'O'):
            return -1  # Opponent wins

    return 0  # Draw

# Function to select individuals for reproduction based on their fitness
def selection(population, opponent_moves):
    # Select individuals for reproduction based on their fitness
    # Here, we use tournament selection
    tournament_size = 5
    selected_population = []

    for _ in range(POPULATION_SIZE):
        tournament = random.sample(population, tournament_size)
        best_individual = max(tournament, key=lambda ind: calculate_fitness(ind, opponent_moves))
        selected_population.append(best_individual)

    return selected_population

# Function to perform crossover between two parents to create offspring
def crossover(parent1, parent2):
    # Perform crossover to create offspring
    # Here, we use one-point crossover
    crossover_point = random.randint(1, BOARD_SIZE * BOARD_SIZE - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

# Function to apply mutation to an individual
def mutate(individual):
    # Apply mutation to the individual with a certain probability
    for i in range(BOARD_SIZE * BOARD_SIZE):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(['X', 'O', ''])

    return individual

# Genetic Algorithm
def genetic_algorithm(opponent_moves):
    # Initialize population
    population = [initialize_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        # Set the first move of the AI at index 0,0 for each individual
        for individual in population:
            individual[0] = 'X'

        # Calculate fitness for each individual in the population
        fitness_scores = [calculate_fitness(individual, opponent_moves) for individual in population]

        # Select individuals for reproduction
        selected_population = selection(population, opponent_moves)

        # Create offspring through crossover and mutation
        offspring_population = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            offspring_population.extend([child1, child2])

        # Replace the old population with the new one
        population = offspring_population

        # Print the best individual's fitness in each generation
        best_fitness = max(fitness_scores)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    # Return the best individual at the end of the evolution
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    return best_individual

# Example usage:
# opponent_moves is initially an empty board
opponent_moves = [''] * (BOARD_SIZE * BOARD_SIZE)
best_individual = genetic_algorithm(opponent_moves)
print("Best Individual:", best_individual)
