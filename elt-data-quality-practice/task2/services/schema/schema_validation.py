import pandas as pd

class SchemaValidation:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def validate_column_names(self, schema: dict[str, str]) -> dict[str, list[str]]:
        df_columns = set(self.df.columns)
        expected_columns = set(schema.keys())
        missing_columns = expected_columns - df_columns
        extra_columns = df_columns - expected_columns
        return {"missing_columns": list(missing_columns), "extra_columns": list(extra_columns)}

    def validate_data_types(self, type_schema: dict[str, str]) -> dict[str, dict[str, str]]:
        mismatched_types = {}
        type_mapping = {
            "int": "int64",
            "float": "float64",
            "str": "object",
            "date": "datetime64[ns]"
        }
        for column, expected_type in type_schema.items():
            if column in self.df.columns:
                actual_dtype = str(self.df[column].dtype)
                expected_dtype = type_mapping.get(expected_type, expected_type)
                if actual_dtype != expected_dtype:
                    mismatched_types[column] = {
                        "expected": expected_dtype,
                        "actual": actual_dtype
                    }
        return mismatched_types

    def validate_ranges(self, range_schema: dict[str, tuple]) -> str:
        violations = []
        for column, value_range in range_schema.items():
            if column in self.df.columns:
                if self.df[column].dtype == "datetime64[ns]":
                    min_val = pd.to_datetime(value_range[0])
                    max_val = pd.to_datetime(value_range[1])
                else:
                    min_val, max_val = value_range

                invalid_rows = self.df[(self.df[column] < min_val) | (self.df[column] > max_val)]
                if not invalid_rows.empty:
                    violations.append(f"{len(invalid_rows)} invalid rows in column '{column}'.")
            else:
                violations.append(f"Column '{column}' not found in DataFrame.")

        return "All values within expected ranges." if not violations else "\n".join(violations)

    def validate_business_rules(self, column: str, condition) -> tuple[int, int]:
        if column not in self.df.columns:
            return 0, 0
        valid_rows = self.df[self.df[column].apply(condition)]
        invalid_rows = self.df[~self.df[column].apply(condition)]
        return len(invalid_rows), len(valid_rows)
