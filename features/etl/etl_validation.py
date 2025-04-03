from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, sum as spark_sum, avg

class ETLValidation:
    def __init__(self, df_before: DataFrame, df_after: DataFrame):
        self.df_before = df_before
        self.df_after = df_after

    def validate_row_count(self) -> tuple[int, int, bool]:
        count_before = self.df_before.count()
        count_after = self.df_after.count()
        return count_before, count_after, count_before == count_after

    def validate_columns(self) -> dict[str, list[str]]:
        missing_columns = list(set(self.df_before.columns) - set(self.df_after.columns))
        extra_columns = list(set(self.df_after.columns) - set(self.df_before.columns))
        return {"missing": missing_columns, "extra": extra_columns}

    def validate_aggregates(self, column: str) -> dict[str, float]:
        before_stats = self.df_before.select(spark_sum(col(column)).alias("sum"), avg(col(column)).alias("avg")).first()
        after_stats = self.df_after.select(spark_sum(col(column)).alias("sum"), avg(col(column)).alias("avg")).first()
        return {
            "sum_difference": before_stats["sum"] - after_stats["sum"],
            "avg_difference": before_stats["avg"] - after_stats["avg"]
        }

    def validate_completeness(self, key_column: str) -> dict[str, list]:
        before_keys = self.df_before.select(key_column).distinct()
        after_keys = self.df_after.select(key_column).distinct()
        missing_keys = before_keys.subtract(after_keys).rdd.map(lambda row: row[key_column]).collect()
        return {"missing_keys": missing_keys}