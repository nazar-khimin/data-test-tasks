import pytest
import pandas as pd

from src.task4_BMI_calc import calculate_bmi, categorize_bmi


def test_bmi_calculation():
    data = {
        'height': [1.60, 1.75, 1.82],
        'weight': [55, 80, 72]
    }
    df = pd.DataFrame(data)

    df = calculate_bmi(df)

    expected_bmi = [21.484375, 26.122449, 21.736505]
    assert all(df['BMI'].round(6) == expected_bmi), "BMI calculation did not match the expected values."


def test_bmi_categorization():
    data = {
        'height': [1.60, 1.75, 1.82],
        'weight': [55, 80, 72]
    }
    df = pd.DataFrame(data)

    df = calculate_bmi(df)
    df = categorize_bmi(df)

    expected_categories = ['Normal weight', 'Overweight', 'Normal weight']
    assert df[
               'BMI_category'].tolist() == expected_categories, "BMI categorization did not match the expected categories."
