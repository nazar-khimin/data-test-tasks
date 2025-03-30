# post_etl_validation.py

def validate_business_rules(df):
    # Example: Check if age is between 18 and 60
    invalid_data = df.filter((df.age < 18) | (df.age > 60))
    if invalid_data.count() > 0:
        print(f"Found {invalid_data.count()} records violating business rules.")
    else:
        print("Business rules validation passed.")