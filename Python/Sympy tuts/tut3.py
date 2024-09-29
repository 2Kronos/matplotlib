import sympy
import math 
from sympy import symbols, factor, expand, diff, integrate, limit, oo, Eq, solve

x = symbols("x")
y = symbols("y")

# Compiler assumes you will eqaute it to 0
# print(solve(2*x +x +5))

# Here the equation is read as x^2 = 16 solve for x
# print(solve(Eq(x**2, 16)))

# Solving for X 
# print(solve(Eq(x**2, y), x))

# Imaginay numbers
# print(solve(Eq(x**3, 16), x))

print(solve(Eq(x**17, 15), x))
