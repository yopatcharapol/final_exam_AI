import numpy as np

from sympy import symbols, sympify, lambdify

x, y = symbols("x y")

def steepest_descent(initial_guess, learning_rate, iterations, expr):
    x, y = initial_guess

    for i in range(iterations):
        gradient = np.array([expr[1](x,y), expr[2](x,y)])  # Gradient of the function
        update = -learning_rate * gradient  # Update step
        x, y = x + update[0], y + update[1]  # Update parameters

        # Print the current iteration and parameter values
        # print(f"Iteration {i+1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {expr[0](x,y):.4f}")

    return x, y, expr[0](x,y)

# Example usage
initial_guess = [0, 0]
learning_rate = 0.1
iterations = 10000

txt = input()
q = txt.split(",")
print(q)
# expr = sympify(qi for qi in q)
# expr = []
# expr.append(sympify(q[0]))
# expr.append(sympify(q[1]))
# expr.append(sympify(q[2]))
expr = [sympify(qi) for qi in q]
# f = []
# f.append(lambdify((x, y), expr[0]))
# f.append(lambdify((x, y), expr[1]))
# f.append(lambdify((x, y), expr[2]))
f = [lambdify((x,y), expr_) for expr_ in expr]

result = steepest_descent(initial_guess, learning_rate, iterations, f)
print(f"{result[2]:.2f}")

# (x-2)*(x-2) +(y+1)*(y+1), 2*(x-2), 2*(y+1)