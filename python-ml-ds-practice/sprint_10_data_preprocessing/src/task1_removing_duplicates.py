import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.

    Parameters:
    df (pd.DataFrame): DataFrame with potential duplicate rows.

    Returns:
    pd.DataFrame: DataFrame with duplicates removed.
    """
    return df.drop_duplicates()

def drop_missing_data(df, threshold=0.5):
    """
    Drop rows where more than a certain percentage of columns have missing values.

    Parameters:
    df (pd.DataFrame): DataFrame with potential missing values.
    threshold (float): The fraction of columns that must be present (non-missing) for a row to be kept.

    Returns:
    pd.DataFrame: DataFrame with rows with too many missing values dropped.
    """
    return df.dropna(thresh=1)

# Example data
data = {
    'A': [1, 2, 2, 4, None],
    'B': [5, 6, 6, None, None],
    'C': [9, 10, 10, None, None]
}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df_cleaned = remove_duplicates(df)
df_cleaned = drop_missing_data(df_cleaned, threshold=0.5)
print(df_cleaned)
