# LeetCode Problem 322: Coin Change
# URL: https://leetcode.com/problems/coin-change/
# Difficulty: Medium
# Tags: Dynamic Programming, 1D DP
# Approach: Bottom-up tabulation using a 1D DP array to compute the
#           minimum number of coins needed to form the target amount.
# Time Complexity: O(amount × len(coins))
# Space Complexity: O(amount)

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]
