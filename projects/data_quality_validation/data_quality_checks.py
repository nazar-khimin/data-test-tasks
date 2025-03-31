import pandas as pd
import numpy as np
from scipy import stats

class DataQualityChecks:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path, delimiter=",")
            print("Dataset loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error while loading the file: {e}")

    def check_null_values(self):
        null_counts = self.df.isnull().sum()
        return null_counts[null_counts > 0]

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def check_outliers_zscore(self):
        numeric_df = self.df.select_dtypes(include=[np.number])
        z_scores = np.abs(stats.zscore(numeric_df, nan_policy='omit'))
        return (z_scores > 3).sum()

    def check_outliers_iqr(self):
        numeric_df = self.df.select_dtypes(include=[np.number])
        Q1 = numeric_df.quantile(0.25)
        Q3 = numeric_df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum()
        return outliers[outliers > 0]

    def get_dataframe(self):
        return self.df

    def clean_data(self):
        self.df.drop_duplicates(inplace=True)
        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)