import sympy 
import math

from sympy import symbols, factor, expand, diff, integrate, limit, oo

x = symbols("x")
y = symbols("y")

formula = x**2
#--------------------differentiaton--------------#
# print(diff(formula))

# print(diff(x**2 + 5*x +16 + x**5*9 ))

# Here you can differentiate specific  variables
# print(diff(y*x**2 +y **2, x))

# exp = e
# print(diff(sympy.exp(x)))

# print(diff(sympy.sin(x) + sympy.cos(x)))

#--------------------integration---------------#
# print(integrate(formula))
#print(integrate(2**x + 2**y, x))

# You can also specify the range
print(integrate(2**x , (x, 0, 10)))

# Integrtaing with infinity
print(integrate(sympy.sin(x), (x, -oo, oo)))
print(integrate(sympy.sin(x**2), (x, -oo, oo)))

print(integrate(1/(x**4+1), (x, 0, oo)))

#--------------------limits------------------#

# read as what is the value of x as x tend to 0
print(limit(x, x, 0))
print(limit(x, x, 5))

print(limit(x, x, 5))