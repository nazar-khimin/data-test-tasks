import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    desc_stats = df.describe().transpose()
    print("Descriptive Statistics:")
    print(desc_stats)

    # Detecting outliers
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.title('Box Plot for Outliers Detection')
    plt.close()

    # Correlation Matrix and Heatmap
    corr_matrix = df.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title("Correlation Matrix Heatmap")
    plt.close()

# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
