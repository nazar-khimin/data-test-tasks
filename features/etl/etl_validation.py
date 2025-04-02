import pandas as pd


class ETLValidation:
    def __init__(self, df_before: pd.DataFrame, df_after: pd.DataFrame):
        self.df_before = df_before
        self.df_after = df_after

    def validate_row_count(self):
        """Check if row count before and after ETL is the same (if expected)."""
        return len(self.df_before), len(self.df_after), len(self.df_before) == len(self.df_after)

    def validate_columns(self):
        """Ensure all expected columns exist after ETL."""
        missing_columns = set(self.df_before.columns) - set(self.df_after.columns)
        extra_columns = set(self.df_after.columns) - set(self.df_before.columns)
        return {"missing": list(missing_columns), "extra": list(extra_columns)}

    def validate_aggregates(self, column: str):
        """Check sum and average of a numeric column before and after ETL."""
        before_sum = self.df_before[column].sum()
        after_sum = self.df_after[column].sum()
        before_avg = self.df_before[column].mean()
        after_avg = self.df_after[column].mean()

        return {
            "sum_difference": before_sum - after_sum,
            "avg_difference": before_avg - after_avg
        }

    def validate_completeness(self, key_column: str):
        """Check if all key values exist after ETL."""
        missing_keys = set(self.df_before[key_column]) - set(self.df_after[key_column])
        return {"missing_keys": list(missing_keys)}