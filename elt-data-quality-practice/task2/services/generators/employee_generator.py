from datetime import date

import pandas as pd
from faker import Faker
from faker.generator import random
from task2.utls.logger_config import logger

from task2.services.generators.base_faker import create_data


def generate_record(fake: Faker) -> list:
    """
        Generates a single fake employee record.
    """
    id = fake.uuid4()
    name = fake.name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=55)
    salary = random.randint(30000, 150000)
    department_id = random.randint(1, 10)

    return [id, name, date_of_birth, salary, department_id]


def write_to_csv(file_path: str, num_records: int) -> None:
    """
        Generates multiple fake user records and writes them to a CSV file.
    """
    fake = create_data("en_US")
    headers = ["id", "name", "date_of_birth", "salary", "department_id"]

    data = [generate_record(fake) for _ in range(num_records)]
    df = pd.DataFrame(data, columns=headers)

    df.to_csv(file_path, index=False)
    logger.info(f"Wrote {num_records} records to {file_path}")


if __name__ == '__main__':
    logger.info(f"Started data generation for {date.today()}.")

    write_to_csv("../data/employees.csv", num_records=100)