# Problem: Return Missing Balanced Numbers
# Description:
#   Given a list of elements, return a dictionary indicating how many times
#   each element must be added to make all elements occur equally.
#   The dictionary contains only elements that are underrepresented.
#
# Time Complexity: O(n)
# Space Complexity: O(d), where d is the number of unique elements
#
# Author: Thrinai Batchu

def return_missing_balanced_numbers(input):
    dct = {}
    for element in input:
        dct[element] = dct.get(element, 0) + 1

    max_val = max(dct.values())
    result = {}

    for key, value in dct.items():
        diff = max_val - value
        if diff > 0:
            result[key] = diff

    return result
