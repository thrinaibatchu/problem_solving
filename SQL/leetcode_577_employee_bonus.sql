-- LeetCode 577. Employee Bonus
-- Link: https://leetcode.com/problems/employee-bonus/
-- Concept: LEFT JOIN, NULL handling, Conditional Filtering
-- Approach:
--   1. Perform a LEFT JOIN to include all employees, even if they have no bonus.
--   2. Use WHERE clause to filter for employees with no bonus OR bonus ≤ 500.
--   3. Select name and bonus as required in output.
-- Difficulty: Easy
-- Database: MySQL

SELECT name, bonus
FROM employee e
LEFT JOIN bonus b ON e.empId = b.empId
WHERE bonus IS NULL OR bonus <= 500;
