from pyspark.sql import SparkSession

from projects.data_profiling.profiling import generate_statistics
from projects.data_profiling.anomaly_detection import detect_outliers, detect_iqr_outliers


# Initialize Spark session
spark = SparkSession.builder.appName("Data Profiling").getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([(1, 5), (2, 8), (3, 10), (4, 2)], ["id", "value"])

# Run profiling
generate_statistics(df)
detect_outliers(df)
detect_iqr_outliers(df)

spark.stop()
