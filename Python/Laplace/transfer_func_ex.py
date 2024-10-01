import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform

# Define inpusts 
# Firat step (up) starts at 1 sec
U1 = 2/s*sym.exp(-s)

# Ramp (down) starts at 3 sec
U2 = -1/s**2*sym.exp(-3*s)

# Ramp completes at 5 sec
U3 = 1/s**2*sym.exp(-5*s)

G = 5*(s+1)/(s+3)**2

#CalcUlate responses
Y1 = G*U1
Y2 = G*U2
Y3 = G*U3

#inver laplace

u1 = inverse_laplace_transform(U1, s, t)
u2 = inverse_laplace_transform(U2, s, t)
u3 = inverse_laplace_transform(U3, s, t)

y1 = inverse_laplace_transform(Y1, s, t)
y2 = inverse_laplace_transform(Y2, s, t)
y3 = inverse_laplace_transform(Y3, s, t)


tm = np.linspace(0,8,100)
us = np.zeros(len(tm))
ys = np.zeros(len(tm))

for u in [u1,u2,u3]:
    for i in range(len(tm)):
        us[i] += u.subs(t,tm[i])

for y in [y1,y2,y3]:
    for i in range(len(tm)):
        ys[i] += y.subs(t,tm[i])

plt.figure()
plt.plot(tm,us,label='u(t)')
plt.plot(tm,ys,label='y(t)')
plt.xlabel('Time (s)')
plt.legend()
plt.show()

