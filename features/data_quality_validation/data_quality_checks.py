import pandas as pd
from features.utils.logger_config import logger

class DataQualityChecks:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path, delimiter=",")
            logger.info("Dataset loaded successfully.")
        except FileNotFoundError:
            logger.info(f"File not found: {file_path}")
        except Exception as e:
            logger.info(f"Error while loading the file: {e}")

    def check_null_values(self):
        null_counts = self.df.isnull().sum()
        return null_counts[null_counts > 0]

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def get_dataframe(self):
        return self.df