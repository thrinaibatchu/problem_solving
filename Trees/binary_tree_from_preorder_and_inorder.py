# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, hmap)

    def helper(self, P, startP, endP, I, startI, endI, hmap):
        #base case size 0 subarray
        if startP > endP:
            return None

        #size 1 sub-array
        if startP == endP:
            return TreeNode(P[startP])
        
        #recursive case
        root = TreeNode(P[startP])
        rootindex = hmap[P[startP]]
        numleft = rootindex-startI
        numright = endI-rootindex
        root.left = self.helper(P, startP+1, startP+numleft, I, startI,rootindex-1, hmap)
        root.right = self.helper(P, startP+numleft+1, endP, I, rootindex+1, endI, hmap)
        return root