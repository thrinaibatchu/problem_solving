# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        self.result = root.val
        
        while q:
            level_vals = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            self.result = level_vals[0]

        return self.result