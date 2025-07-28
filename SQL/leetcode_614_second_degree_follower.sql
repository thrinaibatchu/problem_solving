-- Problem: LeetCode 614 - Second Degree Follower
-- Link: https://leetcode.com/problems/second-degree-follower/
-- Concepts: Self-Join, Graph Traversal, Filtering, Aggregation
-- Approach:
--   1. A user must appear as both a follower and followee.
--   2. Self-join on the follower-followee relationship.
--   3. Group by second-degree user (who follows AND is followed).
--   4. Count distinct followers for that user.
-- Time Complexity: O(N^2) in worst-case due to self-join
-- Space Complexity: O(1) at SQL layer (relational)

SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM Follow f1
JOIN Follow f2 ON f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower;
