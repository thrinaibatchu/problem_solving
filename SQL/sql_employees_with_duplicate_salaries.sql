-- Custom SQL Query: Find Employees Sharing the Same Salary
-- Concept: GROUP BY, HAVING, JOIN on Aggregates
--
-- Approach:
--   - First, identify salaries that appear more than once using GROUP BY + HAVING COUNT > 1
--   - Then join back to the Employee table to retrieve name and salary for each matching employee
--
-- Time Complexity: O(N log N) for GROUP BY and JOIN (index-dependent)
-- Space Complexity: O(1) extra (temporary subquery result)

SELECT e.name, e.salary
FROM Employee e
JOIN (
    SELECT salary
    FROM Employee
    GROUP BY salary
    HAVING COUNT(*) > 1
) dup ON e.salary = dup.salary;
