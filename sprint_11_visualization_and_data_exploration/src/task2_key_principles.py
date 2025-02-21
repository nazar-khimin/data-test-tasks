import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """

    sns.set_style('darkgrid')

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=data,
        x='x',
        y='y',
        ax=ax
    )

    ax.set(
        xlabel='X-Value',
        ylabel='Y-Parameter',
        title="Dependence of Y-Value on X-Value"
    )
    ax.grid(True)

    plt.close(fig)

    return fig

# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)