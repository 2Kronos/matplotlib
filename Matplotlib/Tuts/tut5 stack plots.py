import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# Corrected colors list
colors = ['red', 'blue', 'orange', 'green']

# Stack plot with labels
plt.stackplot(days, sleeping, eating, working, playing,colors=colors, labels=['sleeping', 'eating', 'working', 'playing'],linewidth = 5 )

plt.xlabel('Days')
plt.ylabel('Hours')
plt.legend(loc='upper left')
plt.show()
