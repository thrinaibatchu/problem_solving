# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        if not root:
            return result[0]
        
        self.dfs(root, result)
        return result[0]

    def dfs(self, node, result):
        #Base case
        if not node.left and not node.right:
            return 0
        
        #recursion case
        mydia, lh, rh = 0, 0, 0
        if node.left:
            lh = self.dfs(node.left, result)
            mydia += lh +1
        
        if node.right:
            rh = self.dfs(node.right, result)
            mydia += rh + 1 

        result[0] = max(result[0], mydia)

        return max(lh, rh) + 1      