from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Generate Post-ETL Data").getOrCreate()

data = [
    (1, "Alice", "HR", 50000, "2025-01-01"),
    (2, "Bob", "Finance", 55000, "2025-01-01"),
    (3, "Charlie", "IT", 60000, "2025-01-01")
]
columns = ["id", "name", "department", "salary", "ingestion_date"]

df = spark.createDataFrame(data, columns)
df.write.parquet("../datasets/etl_output.parquet", mode="overwrite")

spark.stop()