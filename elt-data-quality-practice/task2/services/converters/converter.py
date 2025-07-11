from typing import List

import pandas as pd

from task2.models import Employees


def convert_to_employees(df: pd.DataFrame) -> List[Employees]:
    """
    Converts a Pandas DataFrame into a list of Employees ORM instances,

    Args:
        df (pd.DataFrame): The DataFrame containing employee data.

    Returns:
        List[Employees]: A list of Employees ORM instances created from the DataFrame rows.
    """
    employees = []
    for _, row in df.iterrows():
        # Convert the row to a dictionary
        row_dict = row.to_dict()

        if 'date_of_birth' in row_dict and row_dict['date_of_birth']:
            row_dict['date_of_birth'] = pd.to_datetime(row_dict['date_of_birth']).date()

        employee = Employees(
            name=row_dict.get('name'),
            date_of_birth=row_dict.get('date_of_birth'),
            salary=row_dict.get('salary'),
            department_id=row_dict.get('department_id')
        )
        employees.append(employee)

    return employees

