import numpy as np

from src.task3_other import plot_1d, plot_2d, plot_3d


def test_plots():
    import matplotlib.pyplot as plt

    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)

    try:
        plot_1d(x)
        assert plt.get_fignums() == [], "Figure not closed after 1D plot"
        print("1D plot generated successfully.")
    except Exception as e:
        assert False, f"1D plot generation failed with error: {e}"

    try:
        plot_2d(x, y)
        assert plt.get_fignums() == [], "Figure not closed after 2D plot"
        print("2D scatter plot generated successfully.")
    except Exception as e:
        assert False, f"2D plot generation failed with error: {e}"

    try:
        plot_3d(x, y, z)
        assert plt.get_fignums() == [], "Figure not closed after 3D plot"
        print("3D scatter plot generated successfully.")
    except Exception as e:
        assert False, f"3D plot generation failed with error: {e}"

