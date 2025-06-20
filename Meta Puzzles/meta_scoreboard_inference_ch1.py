# Problem: Meta Puzzle - Scoreboard Inference (Chapter 1)
# Source: https://www.metacareers.com/profile/coding_puzzles
# Level: Easy to Medium
# Tags: Greedy, Math, Inference
#
# Description:
#   Given the scores of N competitors in a programming contest where each problem is worth 1 or 2 points,
#   determine the minimum number of problems that could have resulted in all the observed scores.
#
#   You must cover all scores using combinations of 1s and 2s, and minimize the number of problems.
#
# Approach:
#   - Use as many 2-point problems as possible.
#   - If any score is odd, at least one 1-point problem is needed.
#   - Minimum number of problems = max(score) // 2 + (1 if any score is odd)
#
# Time Complexity: O(N)
# Space Complexity: O(1)
#
# Author: Thrinai Batchu

from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    max_score = max(S)
    one_point_needed = any(score % 2 == 1 for score in S)

    result = max_score // 2
    if one_point_needed:
        result += 1

    return result
