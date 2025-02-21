import pytest
import pandas as pd

from src.task2_simple_imputation import impute_missing_values


def test_impute_mean():
    data = {
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': ['cat', None, 'dog', 'dog']
    }
    df = pd.DataFrame(data)

    df_imputed = impute_missing_values(df)

    assert df_imputed['A'].isnull().sum() == 0, "Missing values in column 'A' were not imputed correctly."
    assert df_imputed['A'][2] == 2.3333333333333335, "Mean imputation did not work as expected for column 'A'."


def test_impute_median():
    data = {
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': ['cat', None, 'dog', 'dog']
    }
    df = pd.DataFrame(data)

    df_imputed = impute_missing_values(df)

    assert df_imputed['B'].isnull().sum() == 0, "Missing values in column 'B' were not imputed correctly."
    assert df_imputed['B'][1] == 7, "Median imputation did not work as expected for column 'B'."


def test_impute_mode():
    data = {
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': ['cat', None, 'dog', 'dog']
    }
    df = pd.DataFrame(data)

    df_imputed = impute_missing_values(df)

    assert df_imputed['C'].isnull().sum() == 0, "Missing values in column 'C' were not imputed correctly."
    assert df_imputed['C'][1] == 'dog', "Mode imputation did not work as expected for column 'C'."
