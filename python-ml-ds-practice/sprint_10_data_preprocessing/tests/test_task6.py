import pytest
import pandas as pd

from src.task6_target_encoding import target_encode_smoothing


def test_target_encoded_column_exists():
    data = {
        'color': ['red', 'blue', 'green', 'red'],
        'target': [1, 0, 0, 1]
    }
    df = pd.DataFrame(data)

    df_encoded = target_encode_smoothing(df, 'color', 'target', k=2)

    assert 'color_encoded' in df_encoded.columns, "Target encoded column was not created."


def test_target_encoding_with_smoothing():
    data = {
        'color': ['red', 'blue', 'green', 'red'],
        'target': [1, 0, 0, 1]
    }
    df = pd.DataFrame(data)

    df_encoded = target_encode_smoothing(df, 'color', 'target', k=2)

    assert df_encoded['color_encoded'].round(3).tolist() == [0.75, 0.333, 0.333, 0.75], "Target encoding with " \
                                                                                        "smoothing did not match " \
                                                                                        "expected values."
