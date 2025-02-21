import pandas as pd


def impute_missing_values(df):
    """
    Impute missing values in the dataset using mean, median, and mode.

    Parameters:
    df (pd.DataFrame): DataFrame with missing values.

    Returns:
    pd.DataFrame: DataFrame with missing values imputed.
    """

    df_imputed = df.copy()

    if 'A' in df_imputed.columns:
        mean_value = df_imputed['A'].mean()
        df_imputed['A'].fillna(mean_value, inplace=True)

    if 'B' in df_imputed.columns:
        median_value = df_imputed['B'].median()
        df_imputed['B'].fillna(median_value, inplace=True)

    if 'C' in df_imputed.columns:
        mode_value = df_imputed['C'].mode()[0]
        df_imputed['C'].fillna(mode_value, inplace=True)
    return df_imputed


# Example data
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': ['cat', None, 'dog', 'dog']
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_imputed = impute_missing_values(df)
print(df_imputed)
