-- Custom SQL Query: Find Names with Exactly Two 'a's (Case-Insensitive)
-- Concept: String Manipulation, LENGTH, REPLACE, LOWER
--
-- Approach:
--   - Convert name to lowercase using LOWER(name)
--   - Remove all 'a' characters using REPLACE
--   - Subtract length of the modified string from original to count 'a's
--   - Filter for a_count = 2 in the outer query
--
-- Time Complexity: O(N * M), where N is the number of rows and M is average string length
-- Space Complexity: O(1) extra (scalar evaluation per row)

SELECT name
FROM (
  SELECT name,
         LENGTH(name) - LENGTH(REPLACE(LOWER(name), 'a', '')) AS a_count
  FROM Users
) AS sub
WHERE a_count = 2;
