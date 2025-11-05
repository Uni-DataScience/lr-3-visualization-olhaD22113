import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
   fig, ax = plt.subplots()
   ax.plot(data, color='blue', linewidth=2)
   ax.set_title("1D Line Plot")
   ax.set_xlabel("Index")
   ax.set_ylabel("Value")
   ax.grid(True)
   plt.close(fig)  
   return fig


def plot_2d(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='green', s=40)
    ax.set_title("2D Scatter Plot of X vs Y")
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.grid(True)
    plt.close(fig)
    return fig


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='red', s=30)
    ax.set_title("3D Scatter Plot of X, Y, Z")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    plt.close(fig)
    return fig



# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
