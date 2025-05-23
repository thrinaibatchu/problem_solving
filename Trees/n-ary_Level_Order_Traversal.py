"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result

        q = deque([root])
        while q:
            level_len = len(q)
            level_vals = []

            for _ in range(level_len):
                node = q.popleft()
                level_vals.append(node.val)

                for child in node.children:
                    q.append(child)
            
            result.append(level_vals)
        
        return result