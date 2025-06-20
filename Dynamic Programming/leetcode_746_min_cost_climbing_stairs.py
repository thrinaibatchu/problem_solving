# LeetCode Problem 746: Min Cost Climbing Stairs
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/
# Difficulty: Easy
# Tags: Dynamic Programming, Bottom-Up DP, Tabulation
# Approach: In-place bottom-up DP modifying the input array
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
