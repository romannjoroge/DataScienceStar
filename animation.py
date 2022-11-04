import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


x_vals = list()
y_vals = list()

def animate(i):
    """
    Function to make a plot at each frame
    """
    global x_vals, y_vals

    x_vals.append(i)
    y_vals.append(random.randint(0, 6))

    plt.cla()
    plt.plot(x_vals, y_vals)
    plt.title('Random Numbers Plot')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()