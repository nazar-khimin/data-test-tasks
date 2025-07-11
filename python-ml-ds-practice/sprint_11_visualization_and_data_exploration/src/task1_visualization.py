import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """

    counted_groups = collections.Counter(data)
    sorted_and_counted = dict(sorted(counted_groups.items()))

    fig, ax = plt.subplots()
    for key, value in sorted_and_counted.items():
        ax.bar(x=key, height=value)
        ax.set(title="Frequency of Groups 'A', 'B', 'C'",
              xlabel = 'Group',
              ylabel = 'Frequency')

    plt.close(fig)

    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
