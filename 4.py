from matplotlib import pyplot as plt
import random
from math import sin,radians
import numpy as np

val = [17,3,77,35]
label = ['Маша','Саша','Даша','Петя']


plt.subplot(2,1,1)
plt.title("Круговая")
plt.pie(val,labels=label)
plt.subplot(2,1,2)
plt.title("Кольцевая")
plt.pie(val,labels=label,wedgeprops=dict(width=0.5))
plt.show()
