-- Attach the flat file database
ATTACH DATABASE 'task2/db/company1.db' AS cp1;

-- Create new schema in company2.db
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    dob DATE NOT NULL,
    salary INTEGER NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(dept_id)
);

-- Insert data from old database
INSERT INTO departments (dept_id, dept_name)
SELECT id, name FROM cp1.departments;

INSERT INTO employees (full_name, dob, salary, department_id)
SELECT name, date_of_birth, salary, department_id
FROM cp1.employees;

DETACH DATABASE cp1;