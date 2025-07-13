-- LeetCode 601. Human Traffic of Stadium
-- Link: https://leetcode.com/problems/human-traffic-of-stadium/
-- Concept: Window Functions, Grouping Sequences, CTE
-- Approach:
--   1. Filter rows with people ≥ 100.
--   2. Use ROW_NUMBER() OVER (ORDER BY id) to assign a virtual index.
--   3. Compute group_key = id - row_number to identify consecutive rows.
--   4. Group by group_key and select groups with at least 3 rows.
--   5. Return all rows from those qualifying groups.
-- Difficulty: Hard
-- Database: MySQL

WITH cte_grouping AS (
    SELECT *, id - row_num AS group_key
    FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS row_num
        FROM stadium
        WHERE people >= 100
    ) a
)
SELECT id, visit_date, people
FROM cte_grouping
WHERE group_key IN (
    SELECT group_key
    FROM cte_grouping
    GROUP BY group_key
    HAVING COUNT(*) >= 3
);
