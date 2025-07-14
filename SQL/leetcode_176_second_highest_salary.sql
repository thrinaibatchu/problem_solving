-- LeetCode 176: Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/
-- Concept: Window Functions, DENSE_RANK(), NULL handling
-- Approach: Use DENSE_RANK() to rank salaries in descending order. 
--           Filter for rank = 2, then take MAX(salary) to handle edge cases.
-- Time Complexity: O(N log N) due to ordering
-- Space Complexity: O(N) for window frame buffer (engine-dependent)

SELECT MAX(salary) AS SecondHighestSalary
FROM (
  SELECT id, salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employee
) a
WHERE a.rnk = 2;
