# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        result = [False]
        self.helper(root, targetSum, result)
        return result[0]
    
    def helper(self, node, target, result):
        if node.left is None and node.right is None:
            if target - node.val == 0:
                result[0] = True
            return

        if node.left and not result[0]:
            self.helper(node.left, target-node.val, result)
        
        if node.right and not result[0]:
            self.helper(node.right, target-node.val, result)        