# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node):
            if not node.left and not node.right:
                return 1
            
            lh, rh = 0, 0
            if node.left:
                lh = helper(node.left)
            
            if node.right:
                rh = helper(node.right)
            
            return max(lh, rh) + 1
        return helper(root)