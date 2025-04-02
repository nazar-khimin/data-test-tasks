class DataProfiler:
    def __init__(self, df):
        self.df = df

    def generate_statistics(self):
        stats = self.df.describe().T
        print("Descriptive Statistics:")
        print(stats)

        print("\nAdditional Statistics:")
        for col in self.df.columns:
            null_count = self.df[col].isnull().sum()
            unique_count = self.df[col].nunique()
            print(f"Column: {col} | Null Count: {null_count} | Unique Count: {unique_count}")
