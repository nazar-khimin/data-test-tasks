import numpy as np
import pandas as pd
from scipy.stats import stats


class OutlierDetection:
    def __init__(self, df):
        self.df = df

    def check_outliers_zscore(self):
        numeric_df = self.df.select_dtypes(include=[np.number])
        z_scores = np.abs(stats.zscore(numeric_df, nan_policy='omit'))
        return (z_scores > 3).sum()

    def check_outliers_iqr(self) -> pd.Series:
        numeric_df: pd.DataFrame = self.df.select_dtypes(include=[np.number])
        Q1: pd.Series = numeric_df.quantile(0.25)
        Q3: pd.Series = numeric_df.quantile(0.75)
        IQR: pd.Series = Q3 - Q1
        outlier_mask: pd.DataFrame = numeric_df[(numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))]
        outliers: pd.Series = outlier_mask.sum()
        return outliers[outliers > 0]
