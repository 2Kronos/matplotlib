import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def u(t):
    return np.where(t >= 0, 1, 0)

# Define the function x(t)
def x(t):
    return 4*(t + 2)*u(t + 2) - 4*t*u(t) - 4*u(t - 2) - 4*(t - 4)*u(t - 4) + 4*(t - 5)*u(t - 5)

# Generate time values
t = np.linspace(-5, 10, 1000)

# Calculate x(t)
x_t = x(t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='x(t)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Plot of x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend()
plt.show()
