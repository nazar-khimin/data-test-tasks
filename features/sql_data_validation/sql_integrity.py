from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col

class SparkDataIntegrityChecks:
    def __init__(self, db_path: str):
        self.spark = SparkSession.builder.getOrCreate()
        try:
            self.df = self.spark.read.format("jdbc").options(
                url=f"jdbc:sqlite:{db_path}",
                dbtable="main",
                driver="org.sqlite.JDBC"
            ).load()
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {db_path}. Error: {e}")

    def validate_table_column(self, table: str, column: str):
        df = self.spark.sql(f"SELECT * FROM {table}")
        if column not in df.columns:
            raise ValueError(f"Column '{column}' does not exist in the table '{table}'.")

    def check_referential_integrity(self, table: str, column: str, ref_table: str, ref_column: str):
        self.validate_table_column(table, column)
        self.validate_table_column(ref_table, ref_column)
        df = self.spark.sql(f"SELECT {column} FROM {table}")
        ref_df = self.spark.sql(f"SELECT {ref_column} FROM {ref_table}")
        violations = df.join(ref_df, df[column] == ref_df[ref_column], "left_anti")
        return violations.count()

    def check_business_rule(self, table: str, column: str, condition: str):
        self.validate_table_column(table, column)
        query = f"SELECT COUNT(*) AS invalid_count FROM {table} WHERE NOT ({condition})"
        invalid_count = self.spark.sql(query).collect()[0]["invalid_count"]
        return invalid_count

    def close(self):
        try:
            self.spark.stop()
        except Exception as e:
            raise RuntimeError(f"Failed to close Spark session: {e}")