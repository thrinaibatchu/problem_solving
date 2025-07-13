# LeetCode 110. Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Concept: DFS, Tree Height, Early Exit Optimization
# Approach:
#   1. Use bottom-up DFS to check balance and compute height in one pass.
#   2. At each node, return a tuple (is_balanced, height).
#   3. If any subtree is unbalanced, propagate False up the call stack.
#   4. Final result is determined by root’s is_balanced status.
# Time Complexity: O(n) – visits each node once
# Space Complexity: O(h) – call stack height, where h is tree depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return True, 0
            
            lb, lh = dfs(node.left)
            if not lb:
                return False, 0
            rb, rh = dfs(node.right)
            if not rb:
                return False, 0

            return abs(lh - rh) < 2, 1 + max(lh, rh)
        
        balanced, _ = dfs(root)
        return balanced(root)[0]
