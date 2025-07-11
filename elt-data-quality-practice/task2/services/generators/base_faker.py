from faker import Faker
from task2.utls.logger_config import logger

def create_data(locale: str) -> Faker:
    """
        Creates a Faker instance for generating localized fake data.
    """
    logger.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)