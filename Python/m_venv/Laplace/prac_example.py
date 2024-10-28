import sympy as sym
sym.init_printing()
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform



# Fractopnal decomposition
u =(1)/(s*((s+(0.5+0.866j))*(s+(0.5-0.866j))))
print(sym.apart(u))

# f =(z *0.8)/((z-0.8)**2 *(z-0.75))
# print(sym.apart(f))