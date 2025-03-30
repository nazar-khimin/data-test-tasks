from pyspark.sql import SparkSession
from projects.etl_data_validation.pre_etl_validation import check_row_count, check_key_constraints
from projects.etl_data_validation.post_etl_validation import validate_business_rules

# Initialize Spark session
spark = SparkSession.builder \
    .appName("ETL Data Validation") \
    .getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([(1, 30), (2, 25), (3, 40)], ["id", "age"])

# Run pre-ETL validation
check_row_count(df, 3)
check_key_constraints(df, "id")

# Run post-ETL validation
validate_business_rules(df)