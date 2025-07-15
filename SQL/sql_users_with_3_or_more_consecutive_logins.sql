-- SQL Query: Users Who Logged In for 3 or More Consecutive Days
-- Concept: Window Functions, Consecutive Date Grouping, ROW_NUMBER Alignment Trick
--
-- Problem:
--   Identify user_ids who logged in for at least 3 consecutive days.
--
-- Approach:
--   - Use ROW_NUMBER() partitioned by user_id to assign sequential login ranks
--   - Subtract rownum from login_date to normalize and detect streaks
--   - Group by user_id and (login_date - rownum) to find consecutive sequences
--   - Filter groups with COUNT >= 3
--
-- Time Complexity: O(N log N) due to ROW_NUMBER and grouping
-- Space Complexity: O(N) for windowed and grouped rows
WITH cte AS (
  SELECT user_id, login_date,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS rownum
  FROM logins
),
grouped AS (
  SELECT user_id,
         DATE_SUB(login_date, INTERVAL rownum DAY) AS group_id
  FROM cte
)
SELECT user_id
FROM grouped
GROUP BY user_id, group_id
HAVING COUNT(*) >= 3;
