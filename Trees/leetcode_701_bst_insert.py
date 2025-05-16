# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if root is None: 
            return newNode

        prev=None
        curr=root
        
        while curr is not None:
            if val < curr.val:
                prev = curr
                curr = curr.left
            elif val > curr.val:
                prev = curr
                curr = curr.right
        
        if val < prev.val:
            prev.left = newNode
        else:
            prev.right = newNode
        
        return root     