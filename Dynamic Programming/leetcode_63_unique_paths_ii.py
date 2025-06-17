# LeetCode Problem 63: Unique Paths II
# URL: https://leetcode.com/problems/unique-paths-ii/
# Difficulty: Medium
# Tags: Dynamic Programming, 2D Grid, Space Optimization
# Approach: Space-optimized bottom-up DP using a 1D array. The solution
#           updates the number of paths in place while handling obstacles
#           row by row, including edge cases for the first column.
# Time Complexity: O(m * n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0] = 1

        for col in range(1, n):
            if obstacleGrid[0][col] == 1:
                break
            dp[col] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[-1]