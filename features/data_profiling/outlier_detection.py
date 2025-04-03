from pyspark.sql import DataFrame
from pyspark.sql.functions import col, mean, stddev


class OutlierDetection:
    def __init__(self, df: DataFrame):
        self.df = df

    def check_outliers_zscore(self) -> dict:
        mean_stddev = self.df.select([mean(col(c)).alias(f"{c}_mean") for c in self.df.columns] +
                                     [stddev(col(c)).alias(f"{c}_stddev") for c in self.df.columns])
        mean_stddev = mean_stddev.collect()[0].asDict()

        outliers = {}
        for column in self.df.columns:
            mean_value = mean_stddev[f"{column}_mean"]
            stddev_value = mean_stddev[f"{column}_stddev"]
            outliers[column] = self.df.filter(
                (col(column) > mean_value + 3 * stddev_value) | (col(column) < mean_value - 3 * stddev_value)
            ).count()

        return outliers

    def check_outliers_iqr(self) -> dict:
        quantiles = self.df.approxQuantile(self.df.columns, [0.25, 0.75], 0.05)

        outliers = {}
        for i, column in enumerate(self.df.columns):
            Q1, Q3 = quantiles[i]
            IQR = Q3 - Q1
            outliers[column] = self.df.filter(
                (col(column) < (Q1 - 1.5 * IQR)) | (col(column) > (Q3 + 1.5 * IQR))
            ).count()

        return outliers