from matplotlib import pyplot as plt
import random

x = ['Ольга','Максим','Владимир','Евгений','Наталья']
y = [random.randint(0,20) for i in range(5)]
plt.subplot(2,1,1)
plt.bar(x,y)

plt.subplot(2,1,2)
plt.barh(x,y)
plt.show()
