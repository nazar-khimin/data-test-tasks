import pandas as pd

class DataQualityChecks:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path, delimiter=",")
            print("Dataset loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error while loading the file: {e}")

    def check_null_values(self):
        null_counts = self.df.isnull().sum()
        return null_counts[null_counts > 0]

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def get_dataframe(self):
        return self.df