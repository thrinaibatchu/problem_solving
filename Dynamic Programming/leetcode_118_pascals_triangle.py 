# LeetCode Problem 118: Pascal's Triangle
# URL: https://leetcode.com/problems/pascals-triangle/
# Difficulty: Easy
# Tags: Dynamic Programming, Combinatorics
# Approach: Initialize each row with 1s, then fill inner elements using
#           Pascal's rule: dp[r][c] = dp[r-1][c-1] + dp[r-1][c]
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for i in range(j + 1)] for j in range(numRows)]
        
        for row in range(2, numRows):
            for col in range(1, len(dp[row]) - 1):
                dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
        
        return dp
