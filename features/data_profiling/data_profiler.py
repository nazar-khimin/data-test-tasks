class DataProfiler:
    def __init__(self, df):
        self.df = df

    def generate_statistics(self):
        stats = self.df.describe().T
        stats_string = f"Descriptive Statistics:\n{stats.to_string()}\n\nAdditional Statistics:\n"
        additional_stats = "\n".join(
            [f"Column: {col} | Null Count: {self.df[col].isnull().sum()} | Unique Count: {self.df[col].nunique()}"
             for col in self.df.columns]
        )
        return stats_string + additional_stats
