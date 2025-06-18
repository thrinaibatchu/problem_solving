# LeetCode Problem 120: Triangle
# URL: https://leetcode.com/problems/triangle/
# Difficulty: Medium
# Tags: Dynamic Programming, 2D DP, Top-Down
# Approach: Top-down DP with a triangular 2D array. Each element is the
#           minimum path sum from the top to that point, based on the
#           minimum of the two possible paths above it.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0 for _ in range(j + 1)] for j in range(m)]
        dp[0][0] = triangle[0][0]

        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + triangle[row][0]
            dp[row][-1] = dp[row - 1][-1] + triangle[row][-1]

        for row in range(2, m):
            for col in range(1, row):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]

        return min(dp[-1])
