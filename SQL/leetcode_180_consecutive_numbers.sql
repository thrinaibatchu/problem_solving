-- LeetCode 180: Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/
--
-- ✅ Problem:
-- Find all numbers that appear at least three times consecutively in the Logs table.
--
-- ✅ Concepts:
-- - Window Functions: LAG(), LEAD()
-- - Common Table Expressions (CTEs)
-- - Pattern detection over ordered data
--
-- 🕒 Time Complexity: O(N)
-- 🛑 Space Complexity: O(N) for the CTE (logical not physical storage)

WITH cte_three_nums AS (
  SELECT
    num,
    LAG(num) OVER (ORDER BY id) AS lag_num,
    LEAD(num) OVER (ORDER BY id) AS lead_num
  FROM Logs
)

SELECT DISTINCT
  num AS ConsecutiveNums
FROM cte_three_nums
WHERE num = lag_num AND num = lead_num;
