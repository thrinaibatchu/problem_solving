"""
LeetCode 653: Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Concepts:
- Binary Search Tree properties
- Inorder / Reverse-Inorder DFS (iterative with stack)
- Two-pointer pattern without materializing the array

Approach:
Use two lazy iterators over the BST:
  1) inorder_nodes(root): yields nodes in ascending order (left -> root -> right)
  2) rev_inorder_nodes(root): yields nodes in descending order (right -> root -> left)
Advance like two pointers:
  - If left.val + right.val < k, move the ascending iterator (need a larger sum)
  - If left.val + right.val > k, move the descending iterator (need a smaller sum)
  - If equal, return True
Ensure we never pair a node with itself by yielding nodes (not just values) and
keeping the invariant left is not right.

Time Complexity: O(n)           # each node is pushed/popped at most once per iterator
Space Complexity: O(h)          # h = tree height, two stacks for the iterators
"""

from typing import Optional, Generator, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False

        def inorder_nodes(node: Optional[TreeNode]):
            stack: List[TreeNode] = []
            curr = node
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                yield curr
                curr = curr.right

        def rev_inorder_nodes(node: Optional[TreeNode]):
            stack: List[TreeNode] = []
            curr = node
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.right
                curr = stack.pop()
                yield curr
                curr = curr.left

        lo_it = inorder_nodes(root)
        hi_it = rev_inorder_nodes(root)
        left = next(lo_it, None)
        right = next(hi_it, None)

        # Two-pointer walk without materializing the sorted list
        while left is not None and right is not None and left is not right:
            s = left.val + right.val
            if s == k:
                return True
            if s < k:
                left = next(lo_it, None)    # need a larger sum
            else:
                right = next(hi_it, None)   # need a smaller sum

        return False
