import sqlite3
from features.utiils import logger

class SQLDataIntegrityChecks:
    def __init__(self, db_path: str):
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            logger.info(f"Connected to database: {db_path}")
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database: {db_path}. Error: {e}")

    def validate_table_column(self, table: str, column: str):
        query = f"PRAGMA table_info({table})"
        self.cursor.execute(query)
        schema_info = self.cursor.fetchall()
        columns = [column_info[1] for column_info in schema_info]
        if column not in columns:
            raise ValueError(f"Column '{column}' does not exist in the table '{table}'.")

    def check_referential_integrity(self, table: str, column: str, ref_table: str, ref_column: str):
        self.validate_table_column(table, column)
        self.validate_table_column(ref_table, ref_column)
        query = f"""
            SELECT t.{column} AS violating_value
            FROM {table} t
            LEFT JOIN {ref_table} r ON t.{column} = r.{ref_column}
            WHERE r.{ref_column} IS NULL
        """
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            missing_count = len(results)
            if missing_count > 0:
                logger.info(f"Referential Integrity Violations: {missing_count}")
                logger.info(f"Violating Values: {results}")
            return missing_count
        except sqlite3.Error as e:
            raise RuntimeError(f"Error in referential integrity check: {e}")

    def check_business_rule(self, table: str, column: str, condition: str):
        self.validate_table_column(table, column)
        query = f"SELECT COUNT(*) AS invalid_count FROM {table} WHERE NOT ({condition})"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise RuntimeError(f"Error in business rule check: {e}")

    def close(self):
        try:
            self.conn.close()
            logger.info("Database connection closed.")
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to close database connection: {e}")
