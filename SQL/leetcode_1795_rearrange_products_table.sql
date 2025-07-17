-- LeetCode Problem 1795: Rearrange Products Table
-- Link: https://leetcode.com/problems/rearrange-products-table/
--
-- Concept: UNPIVOT transformation using UNION ALL
-- Approach:
--   - SELECT each store column separately and rename with store label
--   - Use UNION to stack the results
--   - Exclude NULL prices to meet output requirements
-- Time Complexity: O(n), where n is number of rows
-- Space Complexity: O(1)

SELECT product_id, 'store1' AS store, store1 AS price
FROM products
WHERE store1 IS NOT NULL

UNION

SELECT product_id, 'store2' AS store, store2 AS price
FROM products
WHERE store2 IS NOT NULL

UNION

SELECT product_id, 'store3' AS store, store3 AS price
FROM products
WHERE store3 IS NOT NULL;
