# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = [0]
        if not root:
            return result[0]

        self.dfs(root, result)
        return result[0]

    def dfs(self, node, result):
        #base case
        if not node.left and not node.right:
            result[0] += 1
            return True
        
        #recursive case
        iamunival = True
        if node.left:
            bl = self.dfs(node.left, result)
            if not bl or node.val != node.left.val:
                iamunival = False

        if node.right:
            br = self.dfs(node.right, result)
            if not br or node.val != node.right.val:
                iamunival = False
        
        if iamunival:
            result[0] += 1
        
        return iamunival