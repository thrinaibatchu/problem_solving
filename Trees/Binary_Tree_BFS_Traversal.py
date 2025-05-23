class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        result = []

        while q:
            level_size = len(q)
            level_vals = []

            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(level_vals)
        
        return result