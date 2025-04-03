from pyspark.sql import DataFrame
from pyspark.sql.functions import count, when, col, isnan


class DataQualityChecks:
    def __init__(self, df: DataFrame):
        self.df = df

    def check_null_values(self) -> DataFrame:
        null_counts = self.df.select([
            count(when(col(column).isNull() | isnan(col(column)), column)).alias(column)
            for column in self.df.columns
        ])
        return null_counts

    def check_duplicates(self) -> int:
        duplicates = (
            self.df.groupBy(*self.df.columns)
            .count()
            .filter(col("count") > 1)
        )
        return duplicates.count()

    def get_dataframe(self):
        return self.df
