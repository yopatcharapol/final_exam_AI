import numpy as np

def steepest_descent(initial_guess, learning_rate, iterations):
    x = initial_guess

    for i in range(iterations):
        # x**2 - 1
        gradient = 2*x  # Gradient of the function
        update = -learning_rate * gradient  # Update step
        x = x + update # Update parameters

        # Print the current iteration and parameter values
        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {x**2 - 1:.4f}")

    return x

# Example usage
initial_guess = 0
learning_rate = 0.1
iterations = 100

result = steepest_descent(initial_guess, learning_rate, iterations)