-- LeetCode Problem 1327: List the Products Ordered in a Period
-- Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/
--
-- Concept: Join + Date filter + Aggregation
-- Approach:
--   - Use CTE to sum ordered units per product in February 2020
--   - Join with Products table to get product names
--   - Filter products with total units >= 100
-- Time Complexity: O(n)
-- Space Complexity: O(1)

WITH cte_feb_report AS (
  SELECT product_id, SUM(unit) AS units
  FROM orders
  WHERE order_date LIKE '2020-02-%'
  GROUP BY product_id
)

SELECT product_name, units AS unit
FROM cte_feb_report c
JOIN products p USING (product_id)
WHERE units >= 100;
