import sympy as sym
sym.init_printing()
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform


# Here the t, s specifty you are going from the time domain to the s doamin
u = laplace_transform(5*t, t, s)

print(u[0])

d = inverse_laplace_transform(u[0], s, t)
print(d)