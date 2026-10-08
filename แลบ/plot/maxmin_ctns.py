from matplotlib import pyplot as plt
import numpy as np

f, ax = plt.subplots(1)
x = np.arange(-0.5,8.6,0.1)
y = [16 - (4-xi)**2 for xi in x]
plt.plot([0,0],[-4,16], linewidth=2, color='red' )
plt.plot([-16,16],[0,0], linewidth=2, color='red' )
plt.plot(x, y)

# ax.set_ylim(ymin=0)
# ax.set_xlim(xmin=0)
plt.show()