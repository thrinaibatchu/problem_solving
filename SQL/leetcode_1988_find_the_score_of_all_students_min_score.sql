-- LeetCode 1988: Find the Score of All Students
-- https://leetcode.com/problems/find-the-score-of-all-students/
-- Concept: Aggregation, Conditional Join, NULL Handling
-- Approach: For each school, get MIN(score) from exams where student_count <= capacity.
--           Use LEFT JOIN to include schools with no qualifying scores.
-- Time Complexity: O(n)
-- Space Complexity: O(1)
SELECT 
  school_id, 
  IFNULL(MIN(score), -1) AS score
FROM Schools
LEFT JOIN Exam ON student_count <= capacity
GROUP BY school_id;
