SELECT
    e.emp_id,
    e.full_name,
    e.salary,
    e.department_id,
    d.dept_name,
    COUNT(ep.project_id) AS project_count
FROM employees e
JOIN departments d ON e.department_id = d.dept_id
JOIN employee_projects ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id
HAVING
    e.salary > (
        SELECT AVG(salary)
        FROM employees
        WHERE department_id = e.department_id
    )
    AND COUNT(ep.project_id) > 1;
