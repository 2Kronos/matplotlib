import numpy as np
import matplotlib.pyplot as plt

# Manually define the n values and corresponding u[n] values
n = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
u = [1, 1, 3, 3, 2, 1, 0, -1, -1, -1, 0]  # u[n] = 0 for n < 0, 1 for n >= 0

# Plotting
plt.stem(n, u)  # Removed use_line_collection argument
plt.title('Discrete-Time Unit Step Function')
plt.xlabel('n')
plt.ylabel('u[n]')
plt.xticks(n)  # Set x-ticks to match n values
plt.yticks([0, 1])  # Set y-ticks to 0 and 1
plt.grid()
plt.ylim(-2, 4)  # Set y-limits for better visualization
plt.axhline(0, color='black', lw=0.5, ls='--')  # Add x-axis
plt.axvline(0, color='black', lw=0.5, ls='--')  # Add y-axis

# Show the plot
plt.show()
