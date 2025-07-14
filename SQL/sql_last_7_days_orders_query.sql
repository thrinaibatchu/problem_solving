-- Custom SQL Query: Orders in the Last 7 Days
-- Concept: Date Filtering, CURDATE, DATE_SUB, Interval Logic
--
-- Approach:
--   - Use DATE_SUB(CURDATE(), INTERVAL 7 DAY) to calculate the date 7 days ago
--   - Filter orders where order_date is greater than or equal to that value
--   - Ensures retrieval of all records from the last 7 days (inclusive)
--
-- Time Complexity: O(N) for scanning the Orders table
-- Space Complexity: O(1) additional (single date calculation)

SELECT * 
FROM Orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);
