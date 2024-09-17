import sympy
import math 
from sympy import symbols, factor, expand

# print(math.sqrt(16))
# print(sympy.sqrt(16))

x = symbols("x")
y = symbols("y")

# expression = 2*x+y
# print(expression -x)

expression = 2*( x + y)
print(factor(expression))

expression2 = 2*( x + y)
print(expand(expression))

expression3 = x*( x + y)
print(expand(expression3))