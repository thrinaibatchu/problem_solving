# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result

        self.helper(root, targetSum, result, [])
        return result

    
    def helper(self, node, target, result, slate):
        if node.left is None and node.right is None:
            if target == node.val:
                slate.append(node.val)
                result.append(slate[:])
                slate.pop()
            return
        
        if node.left:
            slate.append(node.val)
            self.helper(node.left, target-node.val, result, slate)
            slate.pop()

        if node.right:
            slate.append(node.val)
            self.helper(node.right, target-node.val, result, slate)
            slate.pop()