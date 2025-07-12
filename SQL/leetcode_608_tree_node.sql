-- LeetCode 608. Tree Node
-- Link: https://leetcode.com/problems/tree-node/
-- Concept: Self Join, Tree Classification, CASE Expression
-- Approach:
--   1. Perform a LEFT JOIN on the tree table with itself to determine if a node has children.
--   2. Use CASE to classify each node as Root, Inner, or Leaf based on:
--      - Root: no parent (p_id IS NULL)
--      - Inner: has parent AND has children
--      - Leaf: has parent BUT no children
--   3. Use DISTINCT to avoid duplicates when nodes have multiple children.
-- Difficulty: Medium
-- Database: MySQL

SELECT DISTINCT 
    a.id, 
    CASE
        WHEN a.p_id IS NULL THEN 'Root'
        WHEN a.p_id IS NOT NULL AND b.id IS NOT NULL THEN 'Inner'
        WHEN a.p_id IS NOT NULL AND b.id IS NULL THEN 'Leaf'
        ELSE 'F'
    END AS type
FROM tree a
LEFT JOIN tree b ON a.id = b.p_id;
