# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        global_bag = [float('-inf')]
        def dfs(node):
            if not node.left and not node.right:
                global_bag[0] = max(global_bag[0], node.val)
                return node.val
            
            ls, rs = 0, 0
            if node.left:
                ls = max(dfs(node.left), 0)
            
            if node.right:
                rs = max(dfs(node.right), 0)

            curr_sum = ls + rs + node.val
            global_bag[0] = max(global_bag[0], curr_sum)

            return node.val + max(ls, rs)
        
        dfs(root)
        return global_bag[0]