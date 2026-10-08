import random
import numpy as np

def initialize_population2(board, size):
    population = [mutate_fixed_numbers(row, size) for row in board]
    import pdb
    pdb.set_trace()
    population = np.asarray(population).transpose(1,0,2)
    return population

def mutate_fixed_numbers(board, size):
    candidates = []
    
    pi = np.asarray(board) == 0
    new_board = np.setdiff1d(range(1,10), board)  
    
    for i in range(size):
        random.shuffle(new_board)
        candidate = np.asarray(board)
        candidate[pi] = new_board
        candidates.append(candidate)
        
    return candidates

def is_valid_sudoku(board):
    num_conflict = 0
    for i in range(9):
        if not is_valid_group(board[i]):
            num_conflict += 1

    # Check each column
    for j in range(9):
        column = [board[i][j] for i in range(9)]
        if not is_valid_group(column):
            num_conflict += 1

    # Check each 3x3 subgrid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if not is_valid_group(subgrid):
                num_conflict += 1

    return num_conflict


def is_valid_group(group):
    seen = set()
    for num in group:
        if num != 0:
            if num in seen:
                return False  # Duplicate number found
            seen.add(num)
    return True


def initialize_population(size):
    populations = []
    for _ in range(size):
        chromosome = list(range(1, 10))
        population = []
        for i in range(1, 10):
            random.shuffle(chromosome)
            population.append(chromosome.copy())
        populations.append(population)
    return np.asarray(populations)

def fitness(board, candidate):
    import pdb
    pdb.set_trace()
    score = ((board - candidate) == 0 ).sum()
    return score

def crossover(parent1, parent2):
    for i in range(9):
        crossover_point = random.randint(1, 8)
        parent1[i][crossover_point:] = [gene for gene in parent2[i] if gene not in parent1[i][:crossover_point]]
    return parent1

def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        mutation_points = random.sample(range(9), 2)
        for i in range(9):
            chromosome[i][mutation_points[0]], chromosome[i][mutation_points[1]] = chromosome[i][mutation_points[1]], chromosome[i][mutation_points[0]]
    return chromosome

def genetic_algorithm(board, population_size=100, generations=3000, mutation_rate=0.5):
    # population = initialize_population(board, population_size)
    population = initialize_population(population_size)
    
    match = (board != 0).sum()
    
    candidates = []
    
    for generation in range(generations):
                
        if generation > 0:
            population = np.asarray(candidates)
        
        population = sorted(population, key=lambda x: fitness(board, x), reverse=True)
        count = fitness(board, population[0])
        
        # population = sorted(population, key=lambda x: is_valid_sudoku(x), reverse=False)
        # count = is_valid_sudoku(population[0])
        
        candidates = population[:population_size//10]
        
        if generation % 100 == 0: 
            print((generation, count))
        
        if count == match:
            
            print((generation, count))
            
            nf = is_valid_sudoku(np.asarray(candidates[0]))
            if nf == 0:
                return candidates[0]
            else:
                print(nf)

        parents = random.choices(candidates, k=population_size//2)

        # Create offspring through crossover
        offspring = []
        for parent1, parent2 in zip(parents[::2], parents[1::2]):
            # import pdb
            # pdb.set_trace()
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            offspring.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
                
        candidates = np.concatenate((parents, offspring), axis =0 )

    # Return the best solution found
    return candidates

def display_board(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = np.array([
        [7, 0, 9, 4, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 0],
        [8, 0, 4, 2, 0, 0, 0, 0, 9],
        [0, 3, 0, 7, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [6, 0, 7, 0, 5, 0, 9, 0, 0],
    ])

    print("Puzzle:")
    display_board(sudoku_board)

    solution = genetic_algorithm(sudoku_board)

    print("\nSolution:")
    # display_board(solution)
    for i in range(9):
        print(solution[i][0])
