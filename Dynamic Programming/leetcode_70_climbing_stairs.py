# LeetCode Problem 70: Climbing Stairs
# Topic: Dynamic Programming
## 🧗 LeetCode 70 – Climbing Stairs

# Problem
# You are climbing a staircase. It takes `n` steps to reach the top.  
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Approach
# - Dynamic Programming with space optimization (O(1) space).
# - We use a sliding window of 3 values to rotate through the last two states needed.
# - Recurrence: `f(n) = f(n-1) + f(n-2)`

class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1 for _ in range(3)]
        for i in range(2, n + 1):
            output[i % 3] = output[(i - 1) % 3] + output[(i - 2) % 3]
        return output[n % 3]