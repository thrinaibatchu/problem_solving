# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, A, start, end):
        #Base case
        if start > end:
            return None
        
        #recursion case
        mid = start + int((end-start)/2)
        root = TreeNode(A[mid])
        root.left = self.helper(A, start, mid-1)
        root.right = self.helper(A, mid+1, end)
        return root 