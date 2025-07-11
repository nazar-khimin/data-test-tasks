-- Create projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    department_id INTEGER
);

-- Create employee_projects table
CREATE TABLE employee_projects (
    emp_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);