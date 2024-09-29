import sympy
import math 
from sympy import symbols, factor, expand, diff, integrate, limit, oo

# print(math.sqrt(16))
# print(sympy.sqrt(16))

x = symbols("x")
y = symbols("y")

formula = x ** 2

#print(diff(x**2 + 5*x +16 +x**5*9))
#print(diff(y*x**2 + y**2, y))
#print(diff(sympy.exp(x))) #e^x
#print(diff(sympy.sin(x) + sympy.cos(x)))

#print(integrate((formula)))
#print(integrate(2**x, (x, 0, 10)))
#print(integrate(sympy.sin(x), (x, -oo, oo)))
#print(integrate(sympy.sin(x**2), (x, -oo, oo)))
#print(integrate(1/(x**4 +1), (x, 0, oo)))

# print(limit(x, x, 0))
# print(limit(x**2, x, 4))

# print(limit(50/x, x, 0))
# print(limit(50/X, X, OO))

# print(limit(sympy.sin(x)/x, x, 0))

print(limit(sympy.sin(x), x, 0))
