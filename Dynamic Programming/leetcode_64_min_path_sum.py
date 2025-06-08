# LeetCode Problem 64: Minimum Path Sum
# URL: https://leetcode.com/problems/minimum-path-sum/
# Difficulty: Medium
# Tags: Dynamic Programming, Grid, Tabulation
# Approach: Bottom-up DP with full 2D table
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # Initialize first column
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # Initialize first row
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        # Fill the rest of the table
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[rows - 1][cols - 1]
