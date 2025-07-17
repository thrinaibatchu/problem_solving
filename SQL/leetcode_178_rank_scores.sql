-- LeetCode 178: Rank Scores
-- https://leetcode.com/problems/rank-scores/
--
-- ✅ Problem:
-- Rank all scores in descending order using dense ranking.
-- Tied scores receive the same rank, and the next rank is consecutive (no gaps).
--
-- ✅ Concepts:
-- - Window Functions: DENSE_RANK()
-- - ORDER BY score DESC for highest-to-lowest ranking
--
-- 🕒 Time Complexity: O(N log N) for sorting scores
-- 🛑 Space Complexity: O(1) (no intermediate tables used)

SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;
