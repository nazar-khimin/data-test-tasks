from pyspark.sql import DataFrame
from pyspark.sql.functions import col, approx_count_distinct

class DataProfiler:
    def __init__(self, df: DataFrame):
        self.df = df

    def generate_statistics(self) -> str:
        stats = self.df.describe()
        stats_string = f"Descriptive Statistics:\n{stats.toPandas().to_string(index=False)}\n\nAdditional Statistics:\n"
        additional_stats = "\n".join([
            f"Column: {col_name} | Null Count: {self.df.filter(col(col_name).isNull()).count()} | Unique Count: {self.df.select(approx_count_distinct(col(col_name))).collect()[0][0]}"
            for col_name in self.df.columns
        ])
        return stats_string + additional_stats
