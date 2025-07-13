-- LeetCode 596. Classes More Than 5 Students
-- Link: https://leetcode.com/problems/classes-more-than-5-students/
-- Concept: GROUP BY, HAVING
-- Approach:
--   1. Group the records by class name using GROUP BY.
--   2. Use HAVING COUNT(*) >= 5 to filter groups with 5 or more students.
--   3. Return only the class name(s).
-- Difficulty: Easy
-- Database: MySQL

SELECT class
FROM courses
GROUP BY class
HAVING COUNT(*) >= 5;
