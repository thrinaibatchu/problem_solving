"""
Meta Problem: Fill in the Blanks
---------------------------------------------------------
Given an array containing null values (represented as `None` in Python),
fill in each `None` with the most recent non-null value.

Problem Type: Array Traversal / Data Imputation
Difficulty: Easy–Medium

Example:
    Input : [1, None, 2, 3, None, None, 5, None]
    Output: [1, 1,    2, 3,    3,    3, 5,    5]

Approach:
    Iterate through the array. Track the most recent non-null value.
    Replace nulls with this most recent value as you traverse.

Time Complexity: O(n)
Space Complexity: O(1) – in-place modification

Author: Thrinai Batchu
"""

from typing import List, Optional

def fill_in_the_blanks(input_lst: List[Optional[int]]) -> List[Optional[int]]:
    """
    Fills None values in the list with the most recent non-None value encountered.

    Args:
        input_lst: List of integers and/or None values.

    Returns:
        Modified list with None values filled in.
    """
    most_recent = None
    for i in range(len(input_lst)):
        if input_lst[i] is not None:
            most_recent = input_lst[i]
        else:
            input_lst[i] = most_recent
    return input_lst