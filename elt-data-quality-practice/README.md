# Interview Test

## Requirement
- You will require a GitHub account.

---

## Task 1: Data Processing with CSV
### Objective:
- Work with large datasets within the QA team.
- Crosscheck data against remote systems.
- Interrogate web APIs for information.

### Instructions:
1. **Input**: A CSV file (`2017.csv`) listing dogs licensed in the US during 2017.
   - **Columns**: `LicenseType`, `Breed`, `Color`, `DogName`, `OwnerZip`, `ExpYear`, `ValidDate`.

2. **Steps**:
   - **Normalize Breeds**: Remove whitespaces and convert breed names to lowercase.
   - **Extract Unique Breeds**: Generate a list of breeds without duplicates.
   - **License Analysis**: Create a list of license counts by `LicenseType` for each unique breed.
   - **Popular Names**: Identify the top 5 most popular dog names and count occurrences.
   - **Bonus**: Create a method to return license details for a given date range.

3. **Note**: Write proper comments explaining each method.

---

## Task 2: Enhanced ETL Script
### Objective:
- ETL process using Python (`pandas` and `SQLAlchemy`).

### Instructions:
1. **Input**:
   - Flat file with columns: `id`, `name`, `date_of_birth`, `salary`, `department_id`.
   - New database with tables:
     - **employees**: `emp_id`, `full_name`, `dob`, `salary`, `department_id`.
     - **departments**: `dept_id`, `dept_name`.

2. **Script Goals**:
   - **Extract**: Read data from the flat file.
   - **Transform**:
     - Perform type conversions.
     - Trim spaces in the data.
   - **Load**:
     - Populate the `employees` table.
     - Populate the `departments` table with unique department IDs and names.

3. **SQL Validations**:
   - Ensure data accuracy and consistency.

---

## Task 3: Data Validation Using SQL
### Objective:
- Validate data migrated to the new database.

### Instructions:
1. Write SQL queries to:
   - Match data between flat file and database tables.
   - Join `employees` and `departments` tables to ensure correct department associations.

---

## Task 4: Database Queries
### Objective:
- Perform SQL-based data analytics and insights.

### Queries:
1. **Departments with Average Salary > $50,000**:
   - Identify departments where the average employee salary exceeds $50,000.

2. **Employees with Above-Average Salary Working on >1 Project**:
   - List employees whose salary is above the average for their department and who are involved in more than one project.

3. **Highest Salary by Department & Related Projects**:
   - Identify employees with the highest salary in each department and the projects they are working on.

---

## Task 5: Data Quality & Performance Testing
### Objective:
- Ensure data migration accuracy and optimize ETL performance.

### Guidelines:
1. **Data Quality**:
   - Perform checks for completeness and accuracy.
   - Verify data formats and relationships.
   - Identify missing or inconsistent values.

2. **Performance Testing**:
   - Test ETL process on large datasets.
   - Measure completion time and identify bottlenecks.
   - Optimize scripts for scalability and efficiency.