ATTACH DATABASE 'task2/db/company1.db' AS c1;
ATTACH DATABASE 'task3/db/company2.db' AS c2;

-- Count rows in both tables
-- SELECT
--     (SELECT COUNT(*) FROM c1.employees) AS company1_count,
--     (SELECT COUNT(*) FROM c2.employees) AS company2_count;

--- Compare from company1 to company2
SELECT
    c1e.*,
    c1d.name AS c1_dept_name,
    c2e.*,
    c2d.dept_name AS c2_dept_name
FROM c1.employees c1e
LEFT JOIN c2.employees c2e ON c1e.name = c2e.full_name
LEFT JOIN c1.departments c1d ON c1e.department_id = c1d.id
LEFT JOIN c2.departments c2d ON c2e.department_id = c2d.dept_id
WHERE c2e.full_name IS NULL
   OR c1e.date_of_birth != c2e.dob
   OR c1e.salary != c2e.salary
   OR c1e.department_id != c2e.department_id

UNION ALL

-- Compare from company2 to company1
SELECT
    c1e.*,
    c1d.name AS c1_dept_name,
    c2e.*,
    c2d.dept_name AS c2_dept_name
FROM c2.employees c2e
LEFT JOIN c1.employees c1e ON c2e.full_name = c1e.name
LEFT JOIN c1.departments c1d ON c1e.department_id = c1d.id
LEFT JOIN c2.departments c2d ON c2e.department_id = c2d.dept_id
WHERE c1e.name IS NULL
   OR c1e.date_of_birth != c2e.dob
   OR c1e.salary != c2e.salary
   OR c1e.department_id != c2e.department_id;

DETACH DATABASE c1;
DETACH DATABASE c2;