def check_duplicates(df):
    duplicate_count = df.groupBy("id").count().filter("count > 1").count()
    if duplicate_count > 0:
        print(f"Found {duplicate_count} duplicates.")
    else:
        print("No duplicates found.")
