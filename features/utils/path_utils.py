from pathlib import Path

from pyspark.sql import SparkSession, DataFrame


class FileLoader:
    ROOT_DIR = Path(__file__).parent.parent.parent

    @staticmethod
    def resolve_path(relative_path: str) -> Path:
        return FileLoader.ROOT_DIR / relative_path

    @staticmethod
    def load_csv_with_delimiter(spark: SparkSession, relative_path: str, delimiter: str = ",") -> DataFrame:
        full_path = FileLoader.resolve_path(relative_path)
        return spark.read.option("header", "true").option("delimiter", delimiter).option("inferSchema", "true").csv(
            str(full_path))