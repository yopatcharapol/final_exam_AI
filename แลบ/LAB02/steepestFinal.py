import numpy as np

def steepest_descent(initial_guess, learning_rate, iterations):
    x, y = initial_guess

    for i in range(iterations):
        gradient = np.array([2 * x + 1 + y, 2 * y - 1 + x])  # Gradient of the function
        update = -learning_rate * gradient  # Update step
        x, y = x + update[0], y + update[1]  # Update parameters

        # Print the current iteration and parameter values
        print(f"Iteration {i+1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {(x**2 + x + y**2 - y + x*y + 1):.4f}")

    return x, y

# Example usage
initial_guess = [0, 0]
learning_rate = 0.1
iterations = 1000

result = steepest_descent(initial_guess, learning_rate, iterations)