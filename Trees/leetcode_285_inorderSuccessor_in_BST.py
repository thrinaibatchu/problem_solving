# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #Case where we should have the successrot in the right subtree
        if p.right is not None:
            curr = p.right
            #Finding min element in the right SubTree
            while curr.left is not None:
                curr = curr.left
            return curr
        
        #Now that we know p doesn't have the right node, we need to look up. Which means we need to start from the root. now make sure to track if there are any left turns from the root and tracke the latest left turn node which would be its ancestor.

        ancestor = None
        curr = root
        while curr != p:
            #this is a left turn
            if p.val < curr.val:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right
        
        return ancestor