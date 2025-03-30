from pyspark.sql import SparkSession
from projects.root_cause_analysis.logging import log_error, log_info
from projects.root_cause_analysis.lineage import track_data_lineage
from projects.root_cause_analysis.monitoring import monitor_pipeline

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Root Cause Analysis & Monitoring") \
    .getOrCreate()

# Sample data
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

# Run root cause analysis
log_info("Data pipeline started.")
track_data_lineage(df, "SourceSystem", "TargetSystem")
monitor_pipeline(df)

# Stop Spark session
spark.stop()