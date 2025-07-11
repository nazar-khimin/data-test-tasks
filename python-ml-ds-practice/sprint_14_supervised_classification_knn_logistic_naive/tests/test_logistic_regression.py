import pytest
import numpy as np
import pandas as pd
from src.logistic_regression import (read_csv, train_logistic_regression, evaluate_model,
)


def test_read_csv(tmp_path):
    """
    Test if the read_csv function correctly loads data.
    """
    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("Feature1,Feature2,Target\n1,2,0\n3,4,1")

    # Load the data
    data = read_csv(csv_file)
    assert not data.empty, "CSV file should not be empty."
    assert list(data.columns) == ["Feature1", "Feature2", "Target"], "CSV file must have correct columns."



def test_train_logistic_regression():
    """
    Test if train_logistic_regression runs successfully.
    """
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 1])

    model = train_logistic_regression(X, y)
    assert model is not None, "Model training failed."


def test_evaluate_model():
    """
    Test the evaluate_model function.
    """
    y_true = np.array([0, 1, 1])
    y_pred = np.array([0, 1, 0])

    metrics = evaluate_model(y_true, y_pred)
    assert "Accuracy" in metrics, "Accuracy metric is missing."
    assert "Precision" in metrics, "Precision metric is missing."
    assert "Recall" in metrics, "Recall metric is missing."
    assert "F1-Score" in metrics, "F1-Score metric is missing."


if __name__ == "__main__":
    pytest.main()
