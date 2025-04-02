def validate_rules_via_sql(df, query):
    result = df.sparkSession.sql(query)
    result.show()
