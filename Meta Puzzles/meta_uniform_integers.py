"""
Meta Problem: Uniform Integers
---------------------------------------------------------
A uniform integer is a positive number where all digits are the same (e.g., 1, 22, 777).
Given a range [A, B], count how many uniform integers lie within the interval.

Example:
    Input : A = 75, B = 300
    Output: 5  (77, 88, 99, 111, 222)

Approach:
    Only generate numbers with repeated digits (e.g., '1', '22', ..., '999999999999').
    Use string multiplication and integer conversion to check valid uniform numbers
    with digit lengths from len(A) to len(B).

Time Complexity: O(1) – constant number of checks (at most 108)
Space Complexity: O(1)

Author: Your Name
"""

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    a_len = len(str(A))
    b_len = len(str(B))
    count = 0
    for length in range(a_len, b_len + 1):
        for digit in range(1, 10):
            num = int(str(digit) * length)
            if A <= num <= B:
                count += 1
    return count


# ----------------- Unit Tests -----------------

if __name__ == "__main__":
    tests = [
        (75, 300, 5),                     # 77, 88, 99, 111, 222
        (1, 9, 9),                        # all single-digit numbers
        (999999999999, 999999999999, 1), # edge case: large uniform number
        (10, 11, 1),                      # only 11 is uniform
        (1, 1000000000000, 108)          # full range, all uniform numbers
    ]

    for idx, (a, b, expected) in enumerate(tests, 1):
        result = getUniformIntegerCountInInterval(a, b)
        assert result == expected, f"Test #{idx} failed: expected {expected}, got {result}"
    print("All tests passed.")
