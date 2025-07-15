-- SQL Query: Find Products Never Sold
-- Concept: LEFT JOIN + IS NULL (Anti-Join Pattern)
--
-- Problem: Return product names that were never ordered.
--
-- Approach:
--   - Use LEFT JOIN to retain all products and attach matching orders (if any)
--   - Filter for rows where order.product_id IS NULL (i.e., no matching order)
--
-- Time Complexity: O(N) assuming indexed joins
-- Space Complexity: O(1) extra (engine-optimized join buffer)
SELECT p.name
FROM products p
LEFT JOIN orders o ON p.id = o.product_id
WHERE o.product_id IS NULL;
