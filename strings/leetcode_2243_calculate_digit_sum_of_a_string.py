# 2243. Calculate Digit Sum of a String
# Approach: Iterative / recursive string rebuild
# Time: O(n * rounds), Space: O(n)

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def helper(s: str) -> str:
            # Base case: if string is short enough, stop
            if len(s) <= k:
                return s

            parts = []
            for i in range(0, len(s), k):
                # sum digits in the chunk
                chunk_sum = sum(int(ch) for ch in s[i:i+k])
                parts.append(str(chunk_sum))

            # recurse with new concatenated string
            return helper("".join(parts))

        return helper(s)