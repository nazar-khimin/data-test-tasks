# ----------------------------
# Function to trim spaces from all string columns
# ----------------------------
import pandas as pd

from task2.utls.function_duration import timeit


@timeit
def trim_all_values(df: pd.DataFrame, schema: dict[str, str]) -> pd.DataFrame:
    """
    Trims leading and trailing spaces for every column in the schema, regardless of the target type.
    """
    for column in schema.keys():
        if column in df.columns:
            # Convert all values to strings and trim spaces
            df[column] = df[column].astype(str).str.strip()
    return df