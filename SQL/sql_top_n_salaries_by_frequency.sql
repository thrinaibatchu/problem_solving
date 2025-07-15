-- SQL: Top N Most Frequent Salaries (With and Without Tie Awareness)
-- Problem: Return the top 3 most frequent salaries from the Employee table.
--
-- ✅ Version 1: Simple LIMIT-based approach (not tie-aware)
-- ✅ Version 2: DENSE_RANK() approach to return all salaries tied in top 3 frequencies
--
-- Time Complexity: O(N log N) for grouping and sorting
-- Space Complexity: O(N) for intermediate rank buffer
-- ✅ Version 1: Top 3 salaries by frequency (Not tie-aware)
SELECT salary
FROM employee
GROUP BY salary
ORDER BY COUNT(*) DESC
LIMIT 3;

-- ✅ Version 2: Top 3 salaries by frequency with DENSE_RANK() (Tie-aware)
WITH salary_counts AS (
  SELECT salary, COUNT(*) AS freq
  FROM employee
  GROUP BY salary
),
ranked AS (
  SELECT salary, DENSE_RANK() OVER (ORDER BY freq DESC) AS rnk
  FROM salary_counts
)
SELECT salary
FROM ranked
WHERE rnk <= 3;
