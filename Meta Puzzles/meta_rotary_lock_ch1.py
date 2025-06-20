# Problem: Meta Puzzle - Rotary Lock (Chapter 1)
# Source: https://www.metacareers.com/profile/coding_puzzles
# Level: Easy to Medium
# Tags: Circular Array, Greedy, Modulo Arithmetic
#
# Description:
#   You are given a circular lock dial with numbers from 1 to N.
#   Starting from position 1, determine the minimum time required
#   to enter a sequence of target positions C. Rotating 1 unit
#   clockwise or counter-clockwise takes 1 second.
#
#   For each target number, rotate in the direction that results
#   in the least time.
#
# Time Complexity: O(M), where M = len(C)
# Space Complexity: O(1)
#
# Author: Thrinai Batchu

from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    result = 0
    curr_pointer = 1

    for nxt_target in C:
        clockwise = abs(nxt_target - curr_pointer)
        anticlockwise = N - clockwise
        result += min(clockwise, anticlockwise)
        curr_pointer = nxt_target

    return result