import sympy as sym
sym.init_printing()
from sympy.abc import z, n
from sympy.series.formal import ztrans, inverse_ztrans

# Fractional decomposition in z-domain
f_z = (0.8 * z) / ((z - 0.8)**2 * (z - 0.75))
print("Fractional decomposition (Z-domain) =", sym.apart(f_z))

# Z-domain to time domain (discrete time)
f_z_time = inverse_ztrans(sym.apart(f_z), z, n)
print("Inverse Z-transform =", f_z_time)

# Substitute n = 11 (discrete time point)
n_value = 11
f_z_at_n_value = f_z_time.subs(n, n_value)
print(f"At n = {n_value}, the expression evaluates to:", f_z_at_n_value)
