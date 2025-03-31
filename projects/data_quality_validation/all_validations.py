from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from projects.data_quality_validation.schema_validation import validate_schema
from projects.data_quality_validation.null_check import check_nulls
from projects.data_quality_validation.duplicate_check import check_duplicates

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityValidation").getOrCreate()

# Sample data
data = [(1, "Alice", 30), (2, "Bob", 25), (3, "Charlie", 35)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

# Define expected schema
expected_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
])

# Run validations
validate_schema(df, expected_schema)
check_nulls(df)
check_duplicates(df)