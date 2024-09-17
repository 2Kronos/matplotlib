import matplotlib.pyplot as plt

x = [1,3,4,7,9,5]
y = [3,6,9,3,0,2]
plt.scatter(x, y, label = 'sactter1', color = 'purple', marker= '*', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()