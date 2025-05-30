# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = [0]
        def dfs(node):
            if not node.left and not node.right:
                return 0
            
            left_path, right_path = 0, 0
            if node.left:
                lh = dfs(node.left)
                if node.left.val == node.val:
                    left_path = lh + 1

            if node.right:
                rh = dfs(node.right)
                if node.right.val == node.val:
                    right_path = rh + 1
            
            count[0] = max(left_path + right_path, count[0])
            return max(left_path, right_path)  

        dfs(root)
        return count[0]