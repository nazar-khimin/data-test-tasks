SELECT
    d.dept_name,
    AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.dept_id
GROUP BY d.dept_id
HAVING AVG(e.salary) > 50000;