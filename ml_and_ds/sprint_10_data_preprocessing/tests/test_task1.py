import pytest
import pandas as pd

from src.task1_removing_duplicates import remove_duplicates, drop_missing_data


def test_remove_duplicates():
    data = {
        'A': [1, 2, 2, 4, None],
        'B': [5, 6, 6, None, None],
        'C': [9, 10, 10, None, None]
    }
    df = pd.DataFrame(data)

    df_cleaned = remove_duplicates(df)

    assert df_cleaned.shape[0] == 4, "Duplicate rows were not removed correctly."


def test_drop_missing_data():
    data = {
        'A': [1, 2, 4, None],
        'B': [5, 6, None, None],
        'C': [9, 10, None, None]
    }
    df = pd.DataFrame(data)

    df_cleaned = drop_missing_data(df, threshold=0.5)

    assert df_cleaned.shape[0] == 3, "Rows with too many missing values were not dropped correctly."
