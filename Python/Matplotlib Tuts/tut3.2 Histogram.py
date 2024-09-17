import matplotlib.pyplot as plt

population_ages = [22,25,45,44,65,23,56,78,94,79,83,94,100,112,123,105,6,8]
# to assign names for all  the data we have provided
#ids = [x for x in range(len(population_ages))]
#bins are conatin elemenst in the same range also helps to condense data

bins = [0, 10, 20, 30, 40, 50,60,70, 80, 90, 100, 110, 120]

plt.hist(population_ages,bins, histtype = 'bar', rwidth=0.78)


plt.xlabel('x')
plt.ylabel('y')
plt.title('histro Graph')
plt.legend()
plt.show()