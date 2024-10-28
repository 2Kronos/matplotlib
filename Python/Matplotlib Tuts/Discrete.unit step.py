import numpy as np
import matplotlib.pyplot as plt

# Manually define the n values and corresponding u[n] values
n = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
u = np.array([0, -1, -1, -1, 0, 1, 2, 3, 3, 1, 1, 0, 0])  # Adjust if necessary

# Time-reversed version of u[n]
u_reversed = np.array([u[len(u) - 1 - i] for i in range(len(u))])  # This reverses u

# Calculate the even and odd components
x_even = 0.5 * (u + u_reversed)
x_odd = 0.5 * (u - u_reversed)

# Calculate sums of even and odd components
sum_even = np.sum(x_even)
sum_odd = np.sum(x_odd)

# Print the sums
print(f"Sum of Even Component: {sum_even}")
print(f"Sum of Odd Component: {sum_odd}")

# Print the calculated even and odd components
print(f"x_even: {x_even}")
print(f"x_odd: {x_odd}")

# Plotting
plt.figure(figsize=(12, 8))

# Plot original unit step function
plt.subplot(3, 1, 1)
plt.stem(n, u, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Original Discrete-Time Unit Step Function')
plt.xlabel('n')
plt.ylabel('u[n]')
plt.xticks(n)
plt.grid()
plt.axhline(0, color='black', lw=1, ls='--')
plt.axvline(0, color='black', lw=1, ls='--')
plt.ylim(-2, 4)  # Adjust y-limits if needed

# Plot time-reversed unit step function
plt.subplot(3, 1, 2)
plt.stem(n, u_reversed, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Time-Reversed Discrete-Time Unit Step Function')
plt.xlabel('n')
plt.ylabel('u[-n]')
plt.xticks(n)
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.ylim(-2, 4)  # Adjust y-limits if needed

# Plot even and odd components
plt.subplot(3, 1, 3)
plt.stem(n, x_even, linefmt='m-', markerfmt='mo', basefmt='r-', label='Even')
plt.stem(n, x_odd, linefmt='c-', markerfmt='co', basefmt='r-', label='Odd')
plt.title('Even and Odd Components of the Discrete-Time Unit Step Function')
plt.xlabel('n')
plt.ylabel('x_even[n] and x_odd[n]')
plt.xticks(n)
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.ylim(-2, 4)  # Adjust y-limits if needed

# Show the plots
plt.tight_layout()
plt.show()
