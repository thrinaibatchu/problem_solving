# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    
    def helper(self, node, result):
        if node is None:
            return
        
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)