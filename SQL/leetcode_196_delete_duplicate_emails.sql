-- LeetCode Problem 196: Delete Duplicate Emails
-- Link: https://leetcode.com/problems/delete-duplicate-emails/
--
-- Concept: Deduplication using ROW_NUMBER in a CTE
-- Approach:
--   - Use ROW_NUMBER to rank emails ordered by id
--   - Keep only the row with rnk = 1
--   - Delete all rows with rnk > 1 using a CTE and DELETE
-- MySQL 8.0+ Required
-- Time Complexity: O(n log n)
-- Space Complexity: O(n)

WITH cte_rank AS (
  SELECT id, email, 
         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id ASC) AS rnk
  FROM person
)
DELETE FROM person 
WHERE id IN (
  SELECT id FROM cte_rank WHERE rnk > 1
);
