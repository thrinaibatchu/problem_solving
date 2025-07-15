-- SQL Query: Employees Earning More Than Department Average
-- Concept: CTEs, AVG Aggregation, JOINs, Filtering on Aggregates
--
-- Problem:
--   Return the names and departments of employees whose salary is greater
--   than the average salary of their respective department.
--
-- Approach:
--   1. Use a CTE to calculate average salary per department
--   2. Use another CTE to join employee and department info
--   3. Join the two CTEs and filter employees where salary > avg_salary
--
-- Time Complexity: O(N) for department aggregation and joins
-- Space Complexity: O(1) extra (CTEs are engine-optimized views)

WITH cte_dept_avg_salary AS (
    SELECT departmentId, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY departmentId
),
cte_names_salary AS (
    SELECT e.name AS Employee, d.name AS Department, e.departmentId, e.salary
    FROM employee e
    JOIN department d ON e.departmentId = d.id
)
SELECT b.Employee, b.Department
FROM cte_dept_avg_salary a
JOIN cte_names_salary b ON a.departmentId = b.departmentId
WHERE b.salary > a.avg_salary;
