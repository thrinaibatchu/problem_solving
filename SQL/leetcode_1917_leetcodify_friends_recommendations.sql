-- LeetCode 1917: Leetcoders Recommend Friends from the Same Song
-- Problem: https://leetcode.com/problems/leetcoders-recommend-friends-from-the-same-song/
-- Concepts: SQL, CTEs, JOIN, canonical pair normalization using LEAST/GREATEST
-- Approach:
-- 1. Find user pairs who listened to the same 3+ songs on the same day
-- 2. Normalize user pairs using LEAST/GREATEST to match friendship format
-- 3. LEFT JOIN to exclude existing friendships
-- 4. UNION to return bidirectional recommendations

WITH same_song_pairs AS (
  SELECT 
    LEAST(a.user_id, b.user_id) AS uid1,
    GREATEST(a.user_id, b.user_id) AS uid2,
    COUNT(DISTINCT a.song_id) AS shared_songs
  FROM Listens a
  JOIN Listens b
    ON a.day = b.day
   AND a.song_id = b.song_id
   AND a.user_id < b.user_id
  WHERE a.day = '2021-03-15'
  GROUP BY uid1, uid2
  HAVING shared_songs >= 3
),
non_friends AS (
  SELECT sp.uid1, sp.uid2
  FROM same_song_pairs sp
  LEFT JOIN Friendship f
    ON sp.uid1 = f.user1_id AND sp.uid2 = f.user2_id
  WHERE f.user1_id IS NULL
)
SELECT uid1 AS user_id, uid2 AS recommended_id FROM non_friends
UNION
SELECT uid2 AS user_id, uid1 AS recommended_id FROM non_friends;
