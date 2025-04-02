from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SQL Data Validation") \
    .getOrCreate()

# Sample data
data = [(1, "John", "Doe"), (2, "Alice", "Smith"), (3, "Bob", "Brown")]
columns = ["id", "first_name", "last_name"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Register as SQL Table
df.createOrReplaceTempView("users")

# SQL Validation: Check for duplicate IDs
duplicate_check_query = """
SELECT id, COUNT(*) as count
FROM users
GROUP BY id
HAVING COUNT(*) > 1
"""

duplicates = spark.sql(duplicate_check_query)

if duplicates.count() == 0:
    print("No duplicate IDs found.")
else:
    print("Duplicate IDs detected:")
    duplicates.show()

# SQL Validation: Check if required column exists
required_columns = ["id", "first_name", "last_name"]
for col in required_columns:
    if col not in df.columns:
        print(f"Missing required column: {col}")
    else:
        print(f"Column '{col}' exists.")