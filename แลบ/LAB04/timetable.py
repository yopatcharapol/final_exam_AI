import random

def initialize_schedule(num_students, num_teachers, num_time_slots):
    return [[0] * num_time_slots for _ in range(num_students + num_teachers)]

def fitness(schedule):
    # Example fitness function: maximize free time
    total_free_time = sum(row.count(0) for row in schedule)
    return total_free_time

def crossover(parent1, parent2):
    # Perform single-point crossover
    crossover_point = random.randint(1, len(parent1) - 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(schedule, mutation_rate):
    # Introduce random mutations to the schedule
    for row in schedule:
        for i in range(len(row)):
            if random.random() < mutation_rate:
                row[i] = 1 if row[i] == 0 else 0
    return schedule

def generate_population(population_size, num_students, num_teachers, num_time_slots):
    return [initialize_schedule(num_students, num_teachers, num_time_slots) for _ in range(population_size)]

def select_best_individuals(population, fitness_function, num_selected):
    # Select top individuals based on fitness
    fitness_scores = [(individual, fitness_function(individual)) for individual in population]
    fitness_scores.sort(key=lambda x: x[1], reverse=True)
    return [individual for individual, _ in fitness_scores[:num_selected]]

def genetic_algorithm(population_size, num_generations, num_students, num_teachers, num_time_slots, mutation_rate):
    population = generate_population(population_size, num_students, num_teachers, num_time_slots)

    for generation in range(num_generations):
        # Select the top individuals (parents)
        parents = select_best_individuals(population, fitness, int(0.2 * population_size))

        # Create new offspring through crossover and mutation
        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            child = mutate(crossover(parent1, parent2), mutation_rate)
            offspring.append(child)

        # Replace the old generation with the new generation
        population = parents + offspring

        # Display the best schedule in each generation
        best_schedule = max(population, key=fitness)
        print(f"Generation {generation + 1} - Best Schedule: {best_schedule}, Fitness: {fitness(best_schedule)}")

    # Display the final best schedule
    best_schedule = max(population, key=fitness)
    print(f"Final Best Schedule: {best_schedule}, Fitness: {fitness(best_schedule)}")

if __name__ == "__main__":
    num_students = 30
    num_teachers = 5
    num_time_slots = 40  # Adjust as needed
    population_size = 50
    num_generations = 100
    mutation_rate = 0.1

    genetic_algorithm(population_size, num_generations, num_students, num_teachers, num_time_slots, mutation_rate)
