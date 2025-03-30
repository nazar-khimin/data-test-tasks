from pyspark.sql import functions as F

def check_nulls(df):
    nulls = df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns])
    nulls.show()
