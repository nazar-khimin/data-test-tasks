import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a pandas DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    data = pd.read_csv(file_path)
    if data.empty:
        raise ValueError("The CSV file is empty.")
    return data


def train_logistic_regression(X, y):
    """
    Trains a logistic regression model.

    Parameters:
    X (np.array): Feature matrix.
    y (np.array): Target vector.

    Returns:
    LogisticRegression: Trained logistic regression model.
    """
    model = LogisticRegression()
    model.fit(X, y)
    return model


def evaluate_model(y_true, y_pred):
    """
    Evaluates the model using various metrics.

    Parameters:
    y_true (np.array): True target values.
    y_pred (np.array): Predicted target values.

    Returns:
    dict: Evaluation metrics (accuracy, precision, recall, F1-score).
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return {"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1-Score": f1}


def visualize_decision_boundary(X, y, model):
    """
    Visualizes the data points and decision boundary.

    Parameters:
    X (np.array): Feature matrix.
    y (np.array): Target vector.
    model (LogisticRegression): Trained logistic regression model.
    """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.Paired)
    plt.xlabel('Feature1')
    plt.ylabel('Feature2')
    plt.title('Logistic Regression Decision Boundary')
    plt.show()


if __name__ == "__main__":
    # Step 1: Generate synthetic dataset
    file_path = "../logistic_regression.csv"

    # Step 2: Read the dataset
    data = read_csv(file_path)

    # Step 3: Prepare the data
    X = data[['Feature1', 'Feature2']].values
    y = data['Target'].values

    # Step 4: Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 5: Train logistic regression
    model = train_logistic_regression(X_train, y_train)

    # Step 6: Evaluate the model
    y_pred = model.predict(X_test)
    metrics = evaluate_model(y_test, y_pred)
    print("Model Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")

    # Step 7: Visualize the decision boundary
    visualize_decision_boundary(X_test, y_test, model)
