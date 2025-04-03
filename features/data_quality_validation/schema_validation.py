from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType
from pyspark.sql.functions import col

class SchemaValidation:
    def __init__(self, df):
        self.df = df

    def validate_column_names(self, schema: dict[str, str]) -> dict[str, list[str]]:
        df_columns = set(self.df.columns)
        expected_columns = set(schema.keys())
        missing_columns = expected_columns - df_columns
        extra_columns = df_columns - expected_columns
        return {"missing_columns": list(missing_columns), "extra_columns": list(extra_columns)}

    def validate_data_types(self, type_schema: dict[str, str]) -> dict[str, dict[str, str]]:
        mismatched_types = {}
        spark_type_mapping = {"float": FloatType(), "int": IntegerType()}
        for column, expected_type in type_schema.items():
            if column in self.df.columns:
                actual_type = self.df.schema[column].dataType
                expected_spark_type = spark_type_mapping.get(expected_type, expected_type)
                if not isinstance(actual_type, type(expected_spark_type)):
                    mismatched_types[column] = {
                        "expected": str(expected_spark_type),
                        "actual": str(actual_type),
                    }
        return mismatched_types

    def validate_ranges(self, range_schema: dict[str, tuple[float, float]]) -> str:
        violations = []
        for column, (min_value, max_value) in range_schema.items():
            if column in self.df.columns:
                invalid_count = self.df.filter(
                    (col(column) < min_value) | (col(column) > max_value)
                ).count()
                if invalid_count > 0:
                    violations.append(f"{invalid_count} invalid rows in column '{column}'.")
        return "All values within expected ranges." if not violations else "\n".join(violations)

    def validate_business_rules(self, column: str, condition) -> tuple[int, int]:
        invalid_rows = self.df.filter(condition(col(column)) == False).count()
        valid_rows = self.df.filter(condition(col(column))).count()
        return invalid_rows, valid_rows