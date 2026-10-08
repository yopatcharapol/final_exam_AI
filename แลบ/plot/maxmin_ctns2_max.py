from matplotlib import pyplot as plt
import numpy as np

f, ax = plt.subplots(1)
x = np.arange(-0.5,8.6,0.1)
y = [1 + (4-xi)**2 for xi in x]

plt.text(4, 1, 'Min y = 1 at x = 4', fontsize = 14)

plt.xticks(range(-4, 9))
plt.yticks(range(-4, 17))

plt.plot([0,0],[-4,17], linewidth=2, color='red' )
plt.plot([-4,9],[0,0], linewidth=2, color='red' )
plt.plot(x, y)

# ax.set_ylim(ymin=0)
# ax.set_xlim(xmin=0)
plt.show()