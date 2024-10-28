
yn = 0
a = 0.1

for i in range(0, 24):
    y = a*i+(1-a)*yn
    yn = y
    print(f"y({i}) = {y}")
import sympy as sm
t = sm.symbols('t')
import numpy as np