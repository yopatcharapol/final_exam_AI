import random

def initial_state():
    puzzle = list(range(9))
    random.shuffle(puzzle)
    return puzzle

def fitness(state):
    # Count the number of misplaced tiles
    return sum(1 for i, j in zip(state, range(1, 9)) if i != j)

def crossover(parent1, parent2):
    # Perform single-point crossover
    crossover_point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(state):
    # Swap two random tiles to introduce mutation
    mutated_state = state.copy()
    index1, index2 = random.sample(range(9), 2)
    mutated_state[index1], mutated_state[index2] = mutated_state[index2], mutated_state[index1]
    return mutated_state

def genetic_algorithm():
    population_size = 100
    generations = 1000

    # Initialize the population
    population = [initial_state() for _ in range(population_size)]
    
    for generation in range(generations):
        # Evaluate fitness for each individual in the population
        fitness_scores = [(state, fitness(state)) for state in population]

        import pdb
        pdb.set_trace()
    
        # Sort individuals based on fitness
        fitness_scores.sort(key=lambda x: x[1])

        # Select the top individuals (parents)
        parents = [state for state, _ in fitness_scores[:int(0.2 * population_size)]]

        # Create new offspring through crossover and mutation
        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            offspring.extend([child1, child2])

        # Replace the old generation with the new generation
        population = parents + offspring

        # Check for convergence
        if fitness_scores[0][1] == 0:
            print(f"Solution found in generation {generation + 1}: {fitness_scores[0][0]}")
            break

    best_solution = fitness_scores[0][0]
    print(f"Best solution: {best_solution}")

if __name__ == "__main__":
    genetic_algorithm()