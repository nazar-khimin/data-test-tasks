def check_foreign_key(df, parent_df, child_column, parent_column):
    child_ids = df.select(child_column).distinct().collect()
    parent_ids = parent_df.select(parent_column).distinct().collect()
    missing_ids = [id for id in child_ids if id not in parent_ids]

    if missing_ids:
        print(f"Missing foreign key references: {missing_ids}")
    else:
        print("All foreign key references are valid.")
