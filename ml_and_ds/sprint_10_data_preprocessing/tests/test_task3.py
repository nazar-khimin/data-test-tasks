import pytest
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

from src.task3_data_scaling import apply_min_max_scaling, apply_standard_scaling, apply_robust_scaling


def test_min_max_scaling():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'feature3': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)

    df_min_max_scaled = apply_min_max_scaling(df, ['feature1', 'feature2', 'feature3'])

    assert df_min_max_scaled['feature1'].min() == 0, "Min-Max scaling failed to set minimum to 0 for 'feature1'."
    assert df_min_max_scaled['feature1'].max() == 1, "Min-Max scaling failed to set maximum to 1 for 'feature1'."
    assert df_min_max_scaled['feature2'].min() == 0, "Min-Max scaling failed to set minimum to 0 for 'feature2'."
    assert df_min_max_scaled['feature2'].max() == 1, "Min-Max scaling failed to set maximum to 1 for 'feature2'."
    assert df_min_max_scaled['feature3'].min() == 0, "Min-Max scaling failed to set minimum to 0 for 'feature3'."
    assert df_min_max_scaled['feature3'].max() == 1, "Min-Max scaling failed to set maximum to 1 for 'feature3'."


def test_standard_scaling():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'feature3': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)

    df_standard_scaled = apply_standard_scaling(df, ['feature1', 'feature2', 'feature3'])

    assert pytest.approx(df_standard_scaled['feature1'].mean(),
                         abs=1e-9) == 0, "Standard scaling failed to set mean to 0 for 'feature1'."
    assert pytest.approx(df_standard_scaled['feature1'].std(),
                         rel=0.15) == 1, "Standard scaling failed to set standard deviation to 1 for 'feature1'."
    assert pytest.approx(df_standard_scaled['feature2'].mean(),
                         abs=1e-9) == 0, "Standard scaling failed to set mean to 0 for 'feature2'."
    assert pytest.approx(df_standard_scaled['feature2'].std(),
                         rel=0.15) == 1, "Standard scaling failed to set standard deviation to 1 for 'feature2'."
    assert pytest.approx(df_standard_scaled['feature3'].mean(),
                         abs=1e-9) == 0, "Standard scaling failed to set mean to 0 for 'feature3'."
    assert pytest.approx(df_standard_scaled['feature3'].std(),
                         rel=0.15) == 1, "Standard scaling failed to set standard deviation to 1 for 'feature3'."


def test_robust_scaling():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'feature3': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)

    df_robust_scaled = apply_robust_scaling(df, ['feature1', 'feature2', 'feature3'])

    assert df_robust_scaled['feature1'].median() == 0, "Robust scaling failed to set median to 0 for 'feature1'."
    assert df_robust_scaled['feature2'].median() == 0, "Robust scaling failed to set median to 0 for 'feature2'."
    assert df_robust_scaled['feature3'].median() == 0, "Robust scaling failed to set median to 0 for 'feature3'."
