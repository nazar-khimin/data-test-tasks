import pandas as pd
from plotly.graph_objects import Figure

from src.task5_plotly import create_interactive_plotly


def test_create_interactive_plotly():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    try:
        fig = create_interactive_plotly(df)
        assert isinstance(fig, Figure), "Plotly plot is not a Figure instance."
        print("Plotly interactive plot generated successfully.")
    except Exception as e:
        assert False, f"Plotly plot generation failed with error: {e}"


test_create_interactive_plotly()

