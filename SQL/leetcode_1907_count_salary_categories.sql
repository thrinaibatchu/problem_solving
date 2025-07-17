-- LeetCode Problem 1907: Count Salary Categories
-- Link: https://leetcode.com/problems/count-salary-categories/
--
-- Concept: Classification using CASE + Aggregation
-- Technique: Preserve all possible salary categories using a reference table
-- and RIGHT JOIN to ensure zero-count categories are included.
-- Time Complexity: O(n)
-- Space Complexity: O(1)

WITH cte_sal_category AS (
  SELECT account_id, income,
    CASE
      WHEN income < 20000 THEN 'Low Salary'
      WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
      WHEN income > 50000 THEN 'High Salary'
    END AS category
  FROM accounts
),
reference_categories AS (
  SELECT 'Low Salary' AS category
  UNION ALL
  SELECT 'Average Salary'
  UNION ALL
  SELECT 'High Salary'
)

SELECT category, 
       COUNT(account_id) AS accounts_count 
FROM cte_sal_category
RIGHT JOIN reference_categories USING (category)
GROUP BY category
ORDER BY accounts_count;
