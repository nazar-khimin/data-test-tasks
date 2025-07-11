import polars as pl
from polars import DataFrame


def normalize_breed_names(data: pl.LazyFrame) -> DataFrame:
    """
    Cleans and normalizes breed names using SQL-like operations.
    """
    query = """
            SELECT *, LOWER(REPLACE(Breed, ' ', '')) AS NormalizedBreed
            FROM self
        """
    return data.sql(query).collect()


def extract_unique_breeds(data: pl.DataFrame) -> DataFrame:
    lazy_data = data.lazy()
    query = """
        SELECT DISTINCT NormalizedBreed
        FROM self
    """
    return lazy_data.sql(query).collect()


def licenses_by_breed(data: pl.LazyFrame) -> pl.DataFrame:
    """
    Counts licenses by LicenseType for each breed using SQL-like operations.
    """
    query = """        
        SELECT d."Breed", d."LicenseType", COUNT(*) AS "LicenseCount"
        FROM self AS d
        GROUP BY d."Breed", d."LicenseType"
        ORDER BY "LicenseCount" DESC;
    """
    result = data.sql(query).collect()
    return result


def get_top_names(data: pl.LazyFrame, count: int) -> pl.DataFrame:
    query = f"""        
        SELECT d."DogName", COUNT(*) as name_count
        FROM self as d
        GROUP BY d."DogName"
        ORDER BY name_count DESC
        LIMIT {count};
    """
    result = data.sql(query).collect()
    return result


def get_licenses_by_date_range(data: pl.LazyFrame, start_date: str, end_date: str) -> pl.DataFrame:
    """
    Retrieves license details issued within a given date range
    """
    result = (
        data
        .with_columns(
            pl.col("ValidDate").str.strptime(pl.Datetime, "%m/%d/%Y %H:%M").alias("ParsedDate")
        )
        .filter(
            (pl.col("ParsedDate") >= pl.lit(start_date).str.strptime(pl.Datetime, "%Y-%m-%d")) &
            (pl.col("ParsedDate") <= pl.lit(end_date).str.strptime(pl.Datetime, "%Y-%m-%d"))
        )
        .select(
            "Breed",
            "ParsedDate"
        )
        .sort("ParsedDate")
        .collect()
    )
    return result
