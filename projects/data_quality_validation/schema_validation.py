def validate_schema(df, expected_schema):
    if df.schema == expected_schema:
        print("Schema is valid.")
    else:
        print("Schema does not match.")
        print("Expected schema:", expected_schema)
        print("Actual schema:", df.schema)
