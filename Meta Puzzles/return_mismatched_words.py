# Problem: Return Mismatched Words Between Two Strings
# Description:
#   Given two strings, return a list of words that appear in only one of them (case-sensitive).
#   A word is defined as a sequence of characters separated by spaces.
#   Return the mismatched words from str1 first, then from str2.
#
# Time Complexity: O(n + m), where n = len(str1), m = len(str2)
# Space Complexity: O(n + m)
#
# Author: Thrinai Batchu

def return_mismatched_words(str1, str2):
    result = []

    s1_list = str1.split()
    s2_list = str2.split()

    s1 = set(s1_list)
    s2 = set(s2_list)

    for word in s1_list:
        if word not in s2:
            result.append(word)

    for word in s2_list:
        if word not in s1:
            result.append(word)

    return result