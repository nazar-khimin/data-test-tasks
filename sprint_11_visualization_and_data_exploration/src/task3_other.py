import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(x):
    fig, ax = plt.subplots()
    ax.plot(x)
    ax.set(
        xlabel='X Value',
        ylabel='Function of X',
        title='Line plot of the X values'
    )
    plt.close()
    return fig


def plot_2d(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set(
        xlabel='X Value',
        ylabel='Function of X',
        title='Scatterplot for X from Y values dependency'
    )
    plt.close()
    return fig


def plot_3d(x, y, z):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set(
        title='Sin and Cos from X values',
        xlabel='X Values',
        ylabel='Sin from X Values',
        zlabel='Cosinus from X Values'
    )

    ax.set_zlim(min(z) - 0.1, max(z) + 0.1)
    plt.close()
    return fig
