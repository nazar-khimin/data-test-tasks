import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


def apply_min_max_scaling(df, columns):
    """
    Apply Min-Max Scaling to the specified columns and add the scaled values as new columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to be scaled.
    columns (list of str): List of column names to scale.

    Returns:
    pd.DataFrame: DataFrame with new columns for Min-Max Scaled values.
    """
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled


def apply_standard_scaling(df, columns):
    """
    Apply Z-Score Normalization (Standard Scaling) to the specified columns and add the scaled values as new columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to be scaled.
    columns (list of str): List of column names to scale.

    Returns:
    pd.DataFrame: DataFrame with new columns for Standard Scaled values.
    """
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled


def apply_robust_scaling(df, columns):
    """
    Apply Robust Scaling to the specified columns and add the scaled values as new columns.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to be scaled.
    columns (list of str): List of column names to scale.

    Returns:
    pd.DataFrame: DataFrame with new columns for Robust Scaled values.
    """
    scaler = RobustScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled


# Example data
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [10, 20, 30, 40, 50],
    'feature3': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Apply the scaling functions to the dataset
df_min_max_scaled = apply_min_max_scaling(df, ['feature1', 'feature2', 'feature3'])
df_standard_scaled = apply_standard_scaling(df, ['feature1', 'feature2', 'feature3'])
df_robust_scaled = apply_robust_scaling(df, ['feature1', 'feature2', 'feature3'])

print("Min-Max Scaled Data:")
print(df_min_max_scaled)
print("\nStandard Scaled Data:")
print(df_standard_scaled)
print("\nRobust Scaled Data:")
print(df_robust_scaled)
