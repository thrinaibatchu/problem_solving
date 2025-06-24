# LeetCode 256. Paint House
# https://leetcode.com/problems/paint-house/
#
# Concept: Dynamic Programming (Tabulation)
# Approach: Bottom-up DP where dp[i][j] = min cost to paint house i with color j
# Time Complexity: O(N) where N is the number of houses
# Space Complexity: O(N) for the DP table (can be optimized to O(1))
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        return min(dp[-1])
