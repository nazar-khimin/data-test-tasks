EMPLOYEE_SCHEMA: dict[str, str] = {
    "id": "str",
    "name": "str",
    "date_of_birth": "date",
    "salary": "int",
    "department_id": "int"
}

EMPLOYEE_RANGE_SCHEMA: dict[str, tuple] = {
    "salary": (30000, 150000),
    "department_id": (1, 10),
    "date_of_birth": ("1969-01-01", "2007-01-01")
}