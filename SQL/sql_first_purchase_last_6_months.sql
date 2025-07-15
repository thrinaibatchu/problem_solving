-- SQL Query: First Purchase in Last 6 Months
-- Concept: Window Functions, Filtering with Dates, CTEs
--
-- Problem:
--   Return user_ids whose first purchase occurred in the last 6 months.
--
-- Approach:
--   - Use ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date ASC)
--     to find the first-ever purchase per user.
--   - Filter for rnk = 1 and purchase_date within the last 6 months using DATE_SUB and CURDATE().
--
-- Time Complexity: O(N log N) due to window function
-- Space Complexity: O(N) for CTE row buffer
WITH cte_first_purchase AS (
  SELECT user_id, purchase_date,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date ASC) AS rnk
  FROM purchases
)
SELECT user_id
FROM cte_first_purchase
WHERE rnk = 1
  AND purchase_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 6 MONTH) AND CURDATE();
