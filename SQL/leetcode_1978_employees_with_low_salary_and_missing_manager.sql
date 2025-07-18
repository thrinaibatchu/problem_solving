-- LeetCode Problem 1978 (Variant): Employees with salary < 30000 and missing manager
-- Link: https://leetcode.com/problems/employees-whose-manager-left-the-company/
--
-- Concept: Self-reference integrity + conditional filtering
-- Approach:
--   - Filter employees whose manager_id is not found in employee_id list
--   - Also check salary < 30000
--   - Exclude NULL manager_ids (top-level roles)
-- Time Complexity: O(n)
-- Space Complexity: O(n)

SELECT employee_id
FROM employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  AND manager_id NOT IN (SELECT employee_id FROM employees)
ORDER BY employee_id;
