import os
import pandas as pd
import numpy as np


# Function to check if wine dataset exists and generate corrupted dataset
def generate_wine_datasets():
    original_path = "./wine_quality_original.csv"
    corrupted_path = "./wine_quality_corrupted.csv"

    # Check if the Wine dataset exists locally
    if not os.path.exists(original_path):
        print(f"Error: {original_path} not found. Please place the dataset in the 'datasets' folder.")
        return

    # Load the original dataset to ensure it's valid
    df = pd.read_csv(original_path, delimiter=";")
    print(f"Wine dataset loaded successfully from {original_path}")

    # Optionally, you can introduce synthetic anomalies here (missing values, duplicates, etc.)
    # Example: Adding random missing values to the 'alcohol' column
    np.random.seed(42)
    missing_values_indices = np.random.choice(df.index, size=50, replace=False)
    df.loc[missing_values_indices, 'alcohol'] = np.nan

    # Example: Adding duplicate records
    duplicates = df.sample(n=10, replace=True)  # Fix: `replace=True` creates duplicates
    df = pd.concat([df, duplicates], ignore_index=True)  # Fix: Correct method to combine DataFrames

    # Example: Adding outliers to the 'fixed acidity' column
    outliers = pd.DataFrame({
        'fixed acidity': [20, 25, 30, 40, 50],
        'volatile acidity': [0.5, 0.6, 0.7, 0.8, 0.9],
        'citric acid': [0.2, 0.3, 0.4, 0.5, 0.6],
        'residual sugar': [5.0, 6.0, 7.0, 8.0, 9.0],
        'chlorides': [0.03, 0.04, 0.05, 0.06, 0.07],
        'free sulfur dioxide': [10, 20, 30, 40, 50],
        'total sulfur dioxide': [40, 50, 60, 70, 80],
        'density': [0.99, 1.00, 1.01, 1.02, 1.03],
        'pH': [3.1, 3.2, 3.3, 3.4, 3.5],
        'sulphates': [0.5, 0.6, 0.7, 0.8, 0.9],
        'alcohol': [12, 13, 14, 15, 16]
    })

    # Fix: Use `pd.concat` to combine outliers and the original DataFrame
    df = pd.concat([df, outliers], ignore_index=True)

    # Save the dataset with synthetic anomalies to a separate file
    df.to_csv(corrupted_path, index=False)
    print(f"Synthetic anomalies added and saved to {corrupted_path}")


if __name__ == "__main__":
    generate_wine_datasets()