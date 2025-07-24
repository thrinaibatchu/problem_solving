-- LeetCode 3118: Friday Purchase III
-- Link: https://leetcode.com/problems/friday-purchase-iii/
--
-- Problem:
-- Calculate total spending by Premium and VIP members on each Friday of every week in November 2023.
-- If there are no purchases on a particular Friday, output 0.
--
-- Concepts:
-- - Date filtering using DAYNAME() and calendar week extraction
-- - Canonical week-of-month using FLOOR((DAY(date)-1)/7)+1
-- - Reference table creation for all week-membership combinations
-- - LEFT JOIN to handle missing combinations
-- - IFNULL to plug 0 where data is missing
--
-- Time Complexity: O(n), where n is the number of purchases
-- Space Complexity: O(1) additional structures

WITH cte_query AS (
  SELECT 
    FLOOR((DAY(purchase_date) - 1) / 7) + 1 AS week_of_month,
    membership,
    SUM(amount_spend) AS total_amount
  FROM Purchases p
  JOIN Users u USING (user_id)
  WHERE DAYNAME(purchase_date) = 'Friday'
    AND membership IN ('Premium', 'VIP')
  GROUP BY membership, week_of_month
),
cte_week_of_month AS (
  SELECT 1 AS week_of_month, 'VIP' AS membership
  UNION
  SELECT 2, 'VIP'
  UNION
  SELECT 3, 'VIP'
  UNION
  SELECT 4, 'VIP'
  UNION
  SELECT 1, 'Premium'
  UNION
  SELECT 2, 'Premium'
  UNION
  SELECT 3, 'Premium'
  UNION
  SELECT 4, 'Premium'
)

SELECT 
  a.week_of_month, 
  a.membership,
  IFNULL(q.total_amount, 0) AS total_amount
FROM cte_week_of_month a
LEFT JOIN cte_query q
  USING (week_of_month, membership)
ORDER BY a.week_of_month, a.membership;
