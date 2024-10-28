import sympy as sym
from sympy.abc import s

# Define the expression
u = 1 / (s * ((s + (0.5 + 0.866* sym.I)) * (s + (0.5 - 0.866* sym.I))))

# Perform partial fraction decomposition
decomposed_u = sym.apart(u)

# Extracting coefficients
K1 = decomposed_u.coeff(1/s)
K2 = decomposed_u.coeff(1/(s + (0.5 + 0.866* sym.I)))
K3 = decomposed_u.coeff(1/(s + (0.5 - 0.866* sym.I)))

# Print results with real and imaginary parts
print(f"K1: {K1.evalf()}")
print(f"K2: {K2.evalf()} (in the form a + bj)")
print(f"K3: {K3.evalf()} (in the form a + bj)")

# Pretty print the decomposed form
print("\nPartial fraction decomposition:")
sym.pprint(decomposed_u)
