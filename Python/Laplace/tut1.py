import sympy as sym
sym.init_printing()
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform


# Here the t, s specifty you are going from the time domain to the s doamin
# u = laplace_transform(5*t, t, s)
# print(u[0])

# s domain to time domain
#d = inverse_laplace_transform(u[0], s, t)
# print(d) # The heavisde i.e start at zero

# fractional decomposition
# f =(z *0.8)/((z-0.8)**2 *(z-0.75))
# print(sym.apart(f))

#denominator of transfer function
# d1 = (s+1)*(s+3)*(s**2+3*s+1)
# expand = sym.expand(d1)
# roots = sym.roots(d1)
# print(roots)