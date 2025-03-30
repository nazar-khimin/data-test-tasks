def check_row_count(df, expected_count):
    actual_count = df.count()
    if actual_count == expected_count:
        print(f"Row count matches: {actual_count}")
    else:
        print(f"Row count mismatch! Expected: {expected_count}, Found: {actual_count}")

def check_key_constraints(df, key_column):
    duplicates = df.groupBy(key_column).count().filter("count > 1")
    if duplicates.count() > 0:
        print(f"Key constraint violation found: {duplicates.count()} duplicates")
    else:
        print(f"Key constraints are valid.")
