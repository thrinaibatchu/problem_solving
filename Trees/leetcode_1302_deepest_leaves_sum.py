"""
LeetCode 1302: Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/

Concepts:
- Binary Tree traversal
- BFS (level-order traversal)

Approach:
Use BFS to traverse the tree level by level. For each level, compute the sum 
of all nodes at that depth. The last computed sum corresponds to the deepest leaves.

Time Complexity: O(n)  # each node visited once
Space Complexity: O(w) # queue stores up to the max width of the tree
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level_sum
