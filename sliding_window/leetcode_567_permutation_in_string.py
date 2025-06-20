# Problem: 567. Permutation in String
# Link: https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium
# Tags: Sliding Window, Hashing, String Matching
#
# Given two strings s1 and s2, return True if s2 contains a permutation of s1,
# or False otherwise.
#
# Approach:
# Use a sliding window of size len(s1) over s2 and compare frequency counts.
# We use Counter to store letter frequencies in s1 and in each sliding window
# of s2. As the window slides, update the counts incrementally.
#
# Time Complexity: O(n) where n = len(s2)
# Space Complexity: O(1), since the alphabet is fixed (26 lowercase letters)

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True

        for i in range(len(s1), len(s2)):
            left_char = s2[i - len(s1)]
            right_char = s2[i]

            s2_counter[left_char] -= 1
            if s2_counter[left_char] == 0:
                del s2_counter[left_char]

            s2_counter[right_char] += 1

            if s1_counter == s2_counter:
                return True

        return False
