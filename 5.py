import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], '')

def init():
    ax.set_xlim(-np.pi/4, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    return ln,

def update(frame):
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    xdata = np.linspace(0,5,2000)
    ydata = np.sin(2*np.pi*(xdata-0.01*frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, #frames=np.linspace(0, 2*np.pi, 64),
                    frames = 200,init_func=init, blit=False,interval=25)
plt.show()
