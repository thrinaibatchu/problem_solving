# Problem: Return Smallest Key by N-th Smallest Value
# Source: Internal/Meta-style problem
# Difficulty: Easy to Medium
# Tags: HashMap, Sorting, Lexicographical Order
#
# Description:
# Given a dictionary where keys are strings and values are integers,
# return the key with the n-th smallest value.
# - If multiple keys have the same value, return the one that is lexicographically smallest.
# - If n is 0 or larger than the number of unique values, return None.
#
# Time Complexity: O(N log N), where N is number of keys
# Space Complexity: O(N)
#
# Author: Thrinai Batchu

from collections import defaultdict

def return_smallest_key(inputDict, n):
    if len(inputDict) == 0 or n <= 0:
        return None

    # Group keys by their value
    reverse_map = defaultdict(list)
    for key, value in inputDict.items():
        reverse_map[value].append(key)

    # Sort keys in each value group for lexicographical order
    for key in reverse_map:
        reverse_map[key].sort()

    # Get sorted list of unique values
    sorted_values = sorted(reverse_map.keys())

    if n > len(sorted_values):
        return None

    # Return the first key from the n-th smallest value's list
    return reverse_map[sorted_values[n - 1]][0]
