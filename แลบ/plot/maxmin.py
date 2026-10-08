from matplotlib import pyplot as plt

x = range(0,9)
y = [16 - (4-xi)**2 for xi in x]

plt.plot(x, y)
plt.show()