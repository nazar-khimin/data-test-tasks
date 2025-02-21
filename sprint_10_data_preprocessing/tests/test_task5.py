import pytest
import pandas as pd

from src.task5_one_hot_encoding import group_rare_categories, one_hot_encode


def test_group_rare_categories():
    data = {'color': ['red', 'blue', 'green', 'yellow']}
    df = pd.DataFrame(data)

    df = group_rare_categories(df, 'color', 2)

    assert 'Other' in df['color'].values, "'Other' category was not created correctly for rare categories."


def test_one_hot_encode():
    data = {'color': ['red', 'blue', 'Other']}
    df = pd.DataFrame(data)

    df_encoded = one_hot_encode(df, 'color')

    assert 'color_Other' in df_encoded.columns, "'Other' category was not one-hot encoded correctly."
    assert df_encoded['color_Other'].sum() == 1, "Number of 'Other' category instances did not match expected count."
