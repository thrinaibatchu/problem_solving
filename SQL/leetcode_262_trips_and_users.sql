-- LeetCode 262. Trips and Users
-- Link: https://leetcode.com/problems/trips-and-users/
-- Concept: SQL CTEs, Filtering, IFNULL, RIGHT JOIN
-- Approach:
--   1. Create CTEs to count cancelled and total trips by unbanned users.
--   2. Use RIGHT JOIN to ensure all dates from total trips are included.
--   3. Use IFNULL to handle days with zero cancellations.
--   4. Filter for specific dates in WHERE clause.
-- Difficulty: Hard
-- Database: MySQL

WITH cte_unbanned AS (
    SELECT request_at, COUNT(*) AS cnt
    FROM trips
    WHERE status IN ('cancelled_by_driver', 'cancelled_by_client') 
      AND driver_id IN (SELECT users_id FROM users WHERE banned = 'No') 
      AND client_id IN (SELECT users_id FROM users WHERE banned = 'No')
    GROUP BY request_at
),
cte_total_unbanned AS (
    SELECT request_at, COUNT(*) AS cnt
    FROM trips 
    WHERE driver_id IN (SELECT users_id FROM users WHERE banned = 'No') 
      AND client_id IN (SELECT users_id FROM users WHERE banned = 'No')
    GROUP BY request_at
),
cte_uncancelled_trips AS (
    SELECT request_at, COUNT(*) AS cnt
    FROM trips
    WHERE status = 'completed'
    GROUP BY request_at
)
SELECT 
    b.request_at AS day,
    ROUND(IFNULL(a.cnt, 0) / b.cnt, 2) AS `Cancellation Rate`
FROM cte_unbanned a
RIGHT JOIN cte_total_unbanned b 
    ON a.request_at = b.request_at
WHERE b.request_at IN ('2013-10-01', '2013-10-02', '2013-10-03');
