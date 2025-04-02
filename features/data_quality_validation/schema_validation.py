import pandas as pd


class SchemaValidation:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def validate_column_names(self, schema: dict[str, str]):
        missing_columns = set(schema.keys()) - set(self.df.columns)
        extra_columns = set(schema.keys()) - set(self.df.columns)
        return {"missing_columns": list(missing_columns), "extra_columns": list(extra_columns)}

    def validate_data_types(self, type_schema: dict[str, str]):
        mismatched_types = {}
        type_mapping = {"float": "float64", "int": "int64"}  # Mapping to pandas dtypes

        for column, expected_type in type_schema.items():
            if column in self.df.columns:
                actual_type = str(self.df[column].dtype)
                mapped_expected_type = type_mapping.get(expected_type, expected_type)  # Map expected type

                if actual_type != mapped_expected_type:
                    mismatched_types[column] = {"expected": mapped_expected_type, "actual": actual_type}

        return mismatched_types

    def validate_ranges(self, ranges_schema: dict[str, tuple[float, float]]) -> str:
        violations = []
        for column, (min_value, max_value) in ranges_schema.items():
            if column in self.df.columns:
                invalid_rows = self.df[(self.df[column] < min_value) | (self.df[column] > max_value)]
                if not invalid_rows.empty:
                    violations.append(f"{len(invalid_rows)} invalid rows in column '{column}'.")
        if not violations:
            return "All values within expected ranges."
        else:
            return "\n".join(violations)

    def validate_business_rules(self, column: str, condition):
        invalid_rows = self.df[~self.df[column].apply(condition)]
        valid_rows = self.df[self.df[column].apply(condition)]
        invalid_count = len(invalid_rows)
        valid_count = len(valid_rows)
        return f"{invalid_count} rows violate {column} condition, {valid_count} rows meet the condition."