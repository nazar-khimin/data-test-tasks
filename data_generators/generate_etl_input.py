from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Generate Pre-ETL Data").getOrCreate()

data = [
    (1, "Alice", 30, "HR", 50000),
    (2, "Bob", 25, "Finance", 55000),
    (3, "Charlie", 29, "IT", 60000)
]
columns = ["id", "name", "age", "department", "salary"]

df = spark.createDataFrame(data, columns)
df.coalesce(1).write.parquet("../datasets/etl_input.parquet", mode="overwrite")

spark.stop()