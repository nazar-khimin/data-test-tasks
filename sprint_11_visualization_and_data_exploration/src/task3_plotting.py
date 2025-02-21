import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('1D Plot')
    plt.close()
    return fig


def plot_2d(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('2D Scatter Plot')

    plt.close()
    return fig


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel('X Axis')
    ax.set_xlabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Scatter Plot')

    plt.close()
    return fig


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
