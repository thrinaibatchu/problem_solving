-- LeetCode Problem 1965: Employees With Missing Information
-- Link: https://leetcode.com/problems/employees-with-missing-information/
-- 
-- Concept: Full outer join behavior using LEFT and RIGHT JOIN to find mismatches.
-- Approach:
--   - LEFT JOIN to find employees without salary entries
--   - RIGHT JOIN to find salaries without matching employees
--   - Combine using UNION and order results
-- Time Complexity: O(n + m), where n and m are rows in employees and salaries respectively
-- Space Complexity: O(n), temporary result set

SELECT employee_id
FROM (
    SELECT e.employee_id
    FROM employees e
    LEFT JOIN salaries s ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL

    UNION

    SELECT s.employee_id
    FROM salaries s
    RIGHT JOIN employees e ON e.employee_id = s.employee_id
    WHERE e.name IS NULL
) AS a
ORDER BY employee_id ASC;
