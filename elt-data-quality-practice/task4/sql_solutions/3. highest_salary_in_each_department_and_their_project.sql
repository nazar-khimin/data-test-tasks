SELECT
    e.emp_id,
    e.full_name,
    e.salary,
    d.dept_name,
    p.project_id,
    p.project_name
FROM employees e
JOIN departments d ON e.department_id = d.dept_id
LEFT JOIN employee_projects ep ON e.emp_id = ep.emp_id
LEFT JOIN projects p ON ep.project_id = p.project_id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE department_id = e.department_id
)
ORDER BY d.dept_name, e.emp_id;