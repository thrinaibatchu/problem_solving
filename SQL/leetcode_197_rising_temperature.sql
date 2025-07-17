-- LeetCode Problem 197: Rising Temperature
-- Link: https://leetcode.com/problems/rising-temperature/
--
-- Concept: Compare temperature with the previous day using window functions
-- Approach:
--   1. Use LAG() to access previous temperature in a window frame
--   2. Filter rows where temperature > previous day's temperature
-- Time Complexity: O(n log n) due to sorting by recordDate
-- Space Complexity: O(n) for temporary window buffer

SELECT id
FROM (
  SELECT id, temperature,
         LAG(temperature) OVER (ORDER BY recordDate ASC) AS prev_temp
  FROM Weather
) a
WHERE temperature > prev_temp;
