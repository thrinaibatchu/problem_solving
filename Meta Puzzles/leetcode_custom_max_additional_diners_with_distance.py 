# Problem: Max Additional Diners With Distance Constraint (Custom Problem)
# Link: N/A (Often asked in ByteDance/Google-style interview rounds)
# Concepts: Greedy, Array, Interval Merging
# Approach:
#   1. Sort the existing seated positions.
#   2. For each segment (including before the first seat and after the last),
#      calculate how many new diners can be seated maintaining at least K distance.
#   3. Use integer division to compute max additions per interval.
# Time Complexity: O(M log M + N/K)
# Space Complexity: O(1) extra space (ignoring input)

from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    if M == N:
        return 0

    num_seats = 0
    k_plus = K + 1
    seated = sorted(S)

    if seated[0] > k_plus:
        first = seated[0] - 1
        num_seats += (first // k_plus)

    if seated[-1] < (N - (K + 1)):
        num_seats += ((N - seated[-1]) // k_plus)

    for i in range(0, M):
        if i < M - 1:
            spaces = seated[i + 1] - seated[i]
            if spaces > k_plus:
                num_seats += (spaces // k_plus) - 1

    return num_seats