from matplotlib import pyplot as plt
import random
from math import sin,radians
import numpy as np

x = np.arange(0,720,10)
y = np.sin(np.radians(x))
plt.title("y = sin(x), x = (0,720)")
plt.grid(True)
for i in range(len(y)):
    if y[i] == -1:
        plt.annotate('min',xy=(x[i],y[i]),xycoords='data',
            xytext=(x[i],y[i]+0.5),textcoords='data',arrowprops=dict(facecolor='g'))
    if y[i] == 1:
        plt.annotate('max',xy=(x[i],y[i]),xycoords='data',
            xytext=(x[i],y[i]-0.5),textcoords='data',arrowprops=dict(facecolor='r'))

plt.plot(x,y)
plt.show()
