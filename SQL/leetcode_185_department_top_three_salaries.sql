-- LeetCode 185. Department Top Three Salaries
-- Link: https://leetcode.com/problems/department-top-three-salaries/
-- Concept: SQL Window Function, DENSE_RANK(), CTE
-- Approach: Use DENSE_RANK() partitioned by department name, ordered by salary descending.
-- Filter top 3 ranks in the outer query.
-- Difficulty: Hard
-- Database: MySQL / PostgreSQL compatible


WITH rank_table AS (
    SELECT 
        d.name AS department,
        e.name AS employee,
        e.salary AS salary,
        DENSE_RANK() OVER (
            PARTITION BY d.name 
            ORDER BY e.salary DESC
        ) AS rnk
    FROM employee e
    JOIN department d ON e.departmentId = d.id
)
SELECT department, employee, salary
FROM rank_table
WHERE rnk <= 3
ORDER BY department, salary DESC;
