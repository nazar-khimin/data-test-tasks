import pandas as pd
from matplotlib import pyplot as plt

from src.task2_key_principles import create_scatter_plot


def test_create_scatter_plot():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    try:
        fig = create_scatter_plot(df)
        # Check if the figure and axes are created
        assert isinstance(fig, plt.Figure), "Failed to create a Matplotlib figure."
        print("Scatter plot generated successfully.")
    except Exception as e:
        assert False, f"Scatter plot generation failed with error: {e}"


test_create_scatter_plot()
