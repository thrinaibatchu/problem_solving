-- LeetCode Problem 1587: Bank Account Summary II
-- Link: https://leetcode.com/problems/bank-account-summary-ii/
--
-- Concept: Aggregation with SUM and join to user table
-- Approach:
--   1. Use CTE to compute total transaction amount per account
--   2. Join with users table to get account names
--   3. Filter accounts with balance > 10000
-- Time Complexity: O(n), where n is number of transactions
-- Space Complexity: O(m), where m is number of accounts

WITH cte_balance AS (
    SELECT account, SUM(amount) AS balance
    FROM transactions
    GROUP BY account
)

SELECT name, balance
FROM cte_balance
JOIN users USING (account)
WHERE balance > 10000;
