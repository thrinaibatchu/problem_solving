# Problem: Meta Puzzle - Stack Stabilization (Chapter 1)
# Source: https://www.metacareers.com/profile/coding_puzzles
# Level: Medium
# Tags: Greedy, Array, Stack Validation
#
# Description:
# Given a stack of N inflatable discs with initial radii R[i] (top to bottom),
# determine the minimum number of discs you must deflate so that the stack is stable.
# A stack is stable if each disc is strictly smaller than the disc below it.
#
# You may deflate any disc to a smaller positive integer radius.
# Return -1 if it's impossible to stabilize the stack.
#
# Approach:
# - Traverse the stack from bottom to top.
# - If a disc is too large (R[i] >= R[i+1]), deflate it to R[i+1] - 1.
# - If it becomes <= 0, return -1.
# - Count all such deflations.
#
# Time Complexity: O(N)
# Space Complexity: O(1)
#
# Author: Thrinai Batchu

from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    count = 0
    for i in range(N - 2, -1, -1):
        if R[i] >= R[i + 1]:
            R[i] = R[i + 1] - 1
            count += 1
            if R[i] <= 0:
                return -1
    return count
