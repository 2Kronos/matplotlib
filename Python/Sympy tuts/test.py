from sympy import symbols # type: ignore
from sympy.integrals.transforms import laplace_transform # type: ignore

# Define the symbols
t, s = symbols('t s')

# Define the function
f = t**2

# Compute the Laplace transform
F = laplace_transform(f, t, s)
print(F)
