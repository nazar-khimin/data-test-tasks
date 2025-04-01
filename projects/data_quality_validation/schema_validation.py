import pandas as pd


class SchemaValidation:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_column_names(self, schema: dict[str, str]):
        missing_columns = set(schema.keys()) - set(self.df.columns)
        extra_columns = set(schema.keys()) - set(self.df.columns)
        return {"missing_columns": list(missing_columns), "extra_columns": list(extra_columns)}

    def check_data_types(self, schema: dict[str, str]):
        mismatched_types = {}
        type_mapping = {"float": "float64", "int": "int64"}  # Mapping to pandas dtypes

        for column, expected_type in schema.items():
            if column in self.df.columns:
                actual_type = str(self.df[column].dtype)
                mapped_expected_type = type_mapping.get(expected_type, expected_type)  # Map expected type

                if actual_type != mapped_expected_type:
                    mismatched_types[column] = {"expected": mapped_expected_type, "actual": actual_type}

        return mismatched_types