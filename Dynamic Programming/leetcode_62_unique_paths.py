#leetcode_62_unique_paths.py
# LeetCode Problem 62: Unique Paths
# URL: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium
# Tags: Dynamic Programming, Combinatorics
# Approach: Bottom-up DP using a 2D table
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize first row and first column with 1s
        output = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                output[row][col] = output[row-1][col] + output[row][col-1]
        return output[m-1][n-1]