from matplotlib import pyplot as plt

f, ax = plt.subplots(1)
x = range(0,9)
y = [16 - (4-xi)**2 for xi in x]

plt.plot(x, y)
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
plt.show()