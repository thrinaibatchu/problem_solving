"""
Problem: Frog Hops to Shore
Link: https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/A

Concept:
- Each frog is initially on a lily pad and wants to reach the shore at pad N.
- Frogs can hop forward to the next unoccupied lily pad, possibly jumping over others.
- Only one frog can hop per second.
- Frogs cooperate optimally to minimize the total time.

Approach:
- Each frog needs (N - P[i]) hops to reach the shore in the best case.
- Since only one frog can move per second, the minimum number of seconds needed
  is equal to the maximum (N - P[i]) across all frogs.

Time Complexity: O(F)
Space Complexity: O(1)
"""

from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    max_time = 0
    for val in P:
        hops = N - val
        max_time = max(max_time, hops)
    return max_time
