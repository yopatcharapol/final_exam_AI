from sympy import symbols, sympify, lambdify

x, y = symbols("x y")

txt = input()
q = txt.split()
expr = sympify(q[0]) # 2*x + 2*y - 4

f = lambdify((x, y), expr)

print(f(3, 5))
# 12