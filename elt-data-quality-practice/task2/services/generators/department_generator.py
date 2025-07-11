from typing import List
from task2.models import Departments


def generate_departments(num_records: int) -> List[Departments]:
    """
    Generates a list of meaningful Department instances with unique IDs.
    """
    department_names = [
        "Human Resources", "Engineering", "Marketing", "Sales", "Finance",
        "Operations", "Legal", "Customer Support", "Product Management", "IT"
    ]

    departments = []
    for i in range(1, num_records + 1):
        department_name = department_names[(i - 1) % len(department_names)]

        department = Departments(
            id=i,
            name=department_name
        )
        departments.append(department)
    return departments