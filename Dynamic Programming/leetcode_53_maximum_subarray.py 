# Problem: 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Tags: Dynamic Programming, Kadane's Algorithm
#
# Approach:
#   - Use Kadane’s Algorithm to track the maximum subarray sum.
#   - At each step, decide whether to extend the current subarray or start a new one.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(curr_sum, max_sum)

        return max_sum
