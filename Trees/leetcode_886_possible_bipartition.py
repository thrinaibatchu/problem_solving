# leetcode_886_possible_bipartition.py
# LeetCode Problem 886: Possible Bipartition
# Link: https://leetcode.com/problems/possible-bipartition/
# Name: Possible Bipartition
# Concept: Graphs - BFS coloring, bipartite check
# Approach:
#   - Build adjacency list from the dislikes pairs.
#   - Use BFS to try to color the graph with 2 colors (0 and 1).
#   - If any edge connects two nodes with the same color, bipartition is not possible.
#   - Handles disconnected groups (outer loop).
# Time Complexity: O(N + E), N = people, E = dislikes.
# Space Complexity: O(N + E), for graph and arrays.

from collections import deque
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList=[[] for _ in range(n+1)]
        for v, u in dislikes:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [-1 for _ in range(n+1)]
        
        def bfs(source):
            q = deque([source])

            while q:
                node = q.popleft()
                curr_col = visited[node]
                for neighbor in adjList[node]:
                    #Tree Edge
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1 if curr_col == 0 else 0
                    #Crossedge
                    else:
                        if visited[neighbor] == visited[node]:
                            return False
            
            return True

        for v in range(1, n+1):
            if visited[v] == -1:
                visited[v] = 0
                if not bfs(v):
                    return False
        
        return True