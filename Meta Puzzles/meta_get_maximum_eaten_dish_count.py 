# Problem: Get Maximum Eaten Dish Count
# Source: Meta Puzzles (Internal or Custom)
# Description:
#   You're given a list of dish types arriving in order. You eat a dish only if
#   it hasn't been eaten in the last K dishes. Determine the total number of
#   dishes you will end up eating.
#
# Constraints:
#   - 1 ≤ N ≤ 500,000
#   - 1 ≤ K ≤ N
#   - 1 ≤ D[i] ≤ 1,000,000
#
# Approach:
#   Use a deque to track the last K eaten dishes in order and a set for fast lookup.
#   Only eat a dish if it's not in the recent history.
#
# Time Complexity: O(N)
# Space Complexity: O(K)
#
# Author: Thrinai Batchu

from typing import List
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    if K == N:
        return len(set(D))  # Optimization: all dishes are considered if no recent restriction

    result = 0
    recent_dishes = set()
    history = deque()

    for dish in D:
        if dish not in recent_dishes:
            result += 1
            recent_dishes.add(dish)
            history.append(dish)

            if len(history) > K:
                removed = history.popleft()
                recent_dishes.remove(removed)

    return result
