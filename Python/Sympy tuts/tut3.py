import sympy
import math 
from sympy import symbols, factor, expand, diff, integrate, limit, oo, Eq, solve

s = symbols("s")
# y = symbols("y")

# Compiler assumes you will eqaute it to 0
print(solve(s**3 +s**2*0.3 +1))

# Here the equation is read as x^2 = 16 solve for x
# print(solve(Eq(x**2, 16)))

# Solving for X 
# print(solve(Eq(x**2, y), x))

# Imaginay numbers
# print(solve(Eq(x**3, 16), x))

# print(solve(Eq(x**17, 15), x))
