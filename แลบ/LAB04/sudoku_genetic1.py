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
    population = []
    for _ in range(size):
        chromosome = list(range(1, 10))
        random.shuffle(chromosome)
        population.append(chromosome)
    return np.asarray(population)

def fitness(board, candidate):
    score = ((board - candidate) == 0 ).sum()
    return score

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 8)
    parent1[crossover_point:] = [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return parent1

def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        mutation_points = random.sample(range(9), 2)
        chromosome[mutation_points[0]], chromosome[mutation_points[1]] = chromosome[mutation_points[1]], chromosome[mutation_points[0]]
    return chromosome

def genetic_algorithm(board, population_size=1000, generations=3000, mutation_rate=0.5):
    # population = initialize_population(board, population_size)
    population = initialize_population(population_size)
    
    match = (board != 0).sum()
    
    candidates = []
    
    for generation in range(generations):
        
        count = 0
        
        for i in range(9):
            
            if generation > 0:
                population = candidates[i]
            
            population = sorted(population, key=lambda x: fitness(board[i], x), reverse=True)
            count += fitness(board[i], population[0])
            
            if generation > 0:
                candidates[i] = population[:population_size//10]
            else:
                candidates.append(population[:population_size//10])
        
        if count > 20:
            print((generation, count))
               
        if count == match:
            # Found a solution
            solveboard = []
            for i in range(9):
                solveboard.append(candidates[i][0])
            
            nf = is_valid_sudoku(np.asarray(solveboard))
            if nf == 0:
                return solveboard
            else:
                print(nf)
        
        for i in range(9):
            population = candidates[i]
            parents = random.choices(population, k=population_size//2)

            # Create offspring through crossover
            offspring = []
            for parent1, parent2 in zip(parents[::2], parents[1::2]):
                
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
                offspring.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
                    
            candidates[i] = np.concatenate((parents, offspring), axis =0 )

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
