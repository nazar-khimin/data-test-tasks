from pyspark.sql import functions as F

def generate_statistics(df):
    stats = df.describe().toPandas().set_index('summary').T
    print("Descriptive statistics:")
    print(stats)
    # Additional statistics like null count, unique count, etc.
    for col in df.columns:
        null_count = df.filter(F.col(col).isNull()).count()
        unique_count = df.select(col).distinct().count()
        print(f"Column: {col} | Null count: {null_count} | Unique count: {unique_count}")
