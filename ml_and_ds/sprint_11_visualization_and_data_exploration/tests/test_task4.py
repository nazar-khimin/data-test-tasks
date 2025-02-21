import pandas as pd

from src.task4_exploratory import perform_eda


def test_perform_eda():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    try:
        perform_eda(df)
        print("EDA plots generated successfully.")
    except Exception as e:
        assert False, f"EDA failed with error: {e}"


test_perform_eda()