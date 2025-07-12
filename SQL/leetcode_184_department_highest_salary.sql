-- LeetCode 184. Department Highest Salary
-- Link: https://leetcode.com/problems/department-highest-salary/
-- Concept: SQL Window Function, DENSE_RANK(), CTE
-- Approach: Rank salaries by department using DENSE_RANK(), filter top-ranked employees
-- Difficulty: Medium
-- Database: MySQL / PostgreSQL compatible


WITH rank_table AS (
    SELECT 
        d.name AS department,
        e.name AS employee,
        e.salary AS salary,
        DENSE_RANK() OVER (
            PARTITION BY d.id 
            ORDER BY e.salary DESC
        ) AS rnk
    FROM department d
    JOIN employee e ON d.id = e.departmentId
)
SELECT department, employee, salary
FROM rank_table
WHERE rnk = 1
ORDER BY department;
