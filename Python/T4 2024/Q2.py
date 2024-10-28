import sympy as sym
sym.init_printing()
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform




# fractional decomposition
f = (0.1*s) / ((s-1)**2*(s-0.9))
print("Fractional decomposition =", sym.apart(f))



# s domain to time domain
d = inverse_laplace_transform(sym.apart(f), s, t)
print("laplace",d) # The heavisde i.e start at zero

# Substitute t = 2.8
t_value = 6.43

d_at_t_value = d.subs(t, t_value)
print(f"At t = {t_value}, the expression evaluates to:", d_at_t_value)