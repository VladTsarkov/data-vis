from matplotlib import pyplot as plt
import random
from math import sin,radians,cos
import numpy as np
"""
10) Закрасить пространство между графиками, используя модуль matplotlib
"""
x = np.arange(0,720,10)
y = np.sin(np.radians(x))
y1 = np.cos(np.radians(x))
plt.title("y = sin(x), y1 = cos(x), x = (0,720)")
plt.grid(True)
plt.plot(x,y)
plt.plot(x,y1,'r')
plt.fill_between(x,y,y1).set_facecolor('green')
plt.show()
