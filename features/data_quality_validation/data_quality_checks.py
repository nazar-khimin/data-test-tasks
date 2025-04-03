import logging

import pandas as pd
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import count, when, col, isnan

from features.utils.logger_config import logger


class DataQualityChecks:
    def __init__(self, file_path):
        try:
            self.spark = SparkSession.builder.getOrCreate()
            self.df = self.spark.read.csv(file_path, header=True, inferSchema=True)
            logger.info("Dataset loaded successfully.")
        except Exception as e:
            logger.info(f"Error while loading the file: {e}")

    def check_null_values(self) -> DataFrame:
        null_counts = [
            count(when(col(column).isNull() | isnan(column), column)).alias(column)
            for column in self.df.columns
        ]
        return self.df.select(null_counts)

    def check_duplicate(self) -> int:
        duplicates = (
            self.df.groupBy(self.df.columns)
            .count()
            .filter(col("count") > 1)
        )
        return duplicates.count()

    def get_dataframe(self):
        return self.df
