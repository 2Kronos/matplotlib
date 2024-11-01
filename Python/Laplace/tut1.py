import sympy as sym
sym.init_printing()
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform


# Here the t, s specifty you are going from the time domain to the s doamin
# u = laplace_transform(5*t, t, s)
# print(u[0])

# fractional decomposition
f = (1) / ((s**2*5*(s + 0.2)))
print("Fractional decomposition =", sym.apart(f))



# s domain to time domain
d = inverse_laplace_transform(sym.apart(f), s, t)
print("laplace",d) # The heavisde i.e start at zero

# Substitute t = 2.8
t_value = 2.8

d_at_t_value = d.subs(t, t_value)
print(f"At t = {t_value}, the expression evaluates to:", d_at_t_value)


#denominator of transfer function
# d1 = (s+1)*(s+3)*(s**2+3*s+1)
# expand = sym.expand(d1)
# roots = sym.roots(d1)
# print(roots)