from matplotlib import pyplot as plt
x1 = [1,2,3,4,5]
y1 = [5,4,3,2,1]

x = [1,2,3,4,5]
y = [i*i for i in x]
plt.title(" Лабораторная 1")
plt.grid()
x3 = [1,2,3,4,5]
y3 = [10,5,13,18,2]
plt.plot(x,y,"r--",x3,y3,"y")
plt.plot(x1,y1,linewidth=5)
plt.show()
