import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def read_csv(file_path):
    """
    Reads a CSV file and returns its content as a DataFrame.
    Raises ValueError if the file is empty.
    """
    data = pd.read_csv(file_path)
    if data.empty:
        raise ValueError("The CSV file is empty.")
    return data


def visualize_data(data, x_column, y_column):
    """
    Visualizes the relationship between the feature and the target variable.
    """
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter plot of {y_column} vs {x_column}')
    plt.show()


def linear_regression_with_metrics(data, x_column, y_column):
    """
    Performs linear regression, evaluates metrics, and visualizes the regression line.
    """
    # Prepare the data
    X = data[[x_column]].values
    y = data[y_column].values

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print(f"Model Evaluation Metrics:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    # Visualize the regression line
    plt.scatter(X_test, y_test, color='blue', label='Actual data')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Linear Regression Fit')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Example usage
    csv_path = "../data.csv"  # Path to the dataset
    data = read_csv(csv_path)
    print("Data Loaded Successfully!")

    # Visualize the data
    visualize_data(data, x_column="Feature", y_column="Target")

    # Run Linear Regression and Evaluate Metrics
    linear_regression_with_metrics(data, x_column="Feature", y_column="Target")
