import sqlite3
from faker import Faker
import random

conn = sqlite3.connect("db/company3.db")
cur = conn.cursor()
fake = Faker()

# Fake departments and employees (assumes you have 5 departments and 100 employees already)
department_ids = [1, 2, 3, 4, 5]
employee_ids = list(range(1, 101))

# Generate and insert fake projects
for _ in range(20):  # 20 projects
    name = fake.bs().capitalize()
    dept_id = random.choice(department_ids)
    cur.execute("INSERT INTO projects (project_name, department_id) VALUES (?, ?)", (name, dept_id))

# Fetch generated project IDs
cur.execute("SELECT project_id FROM projects")
project_ids = [row[0] for row in cur.fetchall()]

# Generate employee-project assignments
for _ in range(100):  # 100 assignments
    emp_id = random.choice(employee_ids)
    proj_id = random.choice(project_ids)
    cur.execute("INSERT INTO employee_projects (emp_id, project_id) VALUES (?, ?)", (emp_id, proj_id))

conn.commit()
conn.close()