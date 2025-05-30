# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_val = [None]
        def dfs(node):
            if not node:
                return True
            

            left = dfs(node.left)
            if not left or (last_val[0] is not None and node.val <= last_val[0]):
                return False
            last_val[0] = node.val

            right = dfs(node.right)

            return left and right

        return dfs(root)