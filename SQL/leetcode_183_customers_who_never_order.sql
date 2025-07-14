-- LeetCode 183: Customers Who Never Order
-- https://leetcode.com/problems/customers-who-never-order/
--
-- Concept: LEFT JOIN, NULL filtering, anti-join pattern
-- Approach:
--   - Use LEFT JOIN to find customers who have no matching record in Orders
--   - Filter where Orders.customerId IS NULL to identify customers with no orders
--
-- Alternate: NOT IN (SELECT customerId ...) works but fails when Orders has NULLs
--
-- Time Complexity: O(N) to O(N log N) depending on indexing and join strategy
-- Space Complexity: O(1) additional (engine handles join buffering)

SELECT name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;
