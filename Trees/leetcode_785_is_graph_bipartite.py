# leetcode_785_is_graph_bipartite.py
# LeetCode Problem 785: Is Graph Bipartite?
# Link: https://leetcode.com/problems/is-graph-bipartite/
# Name: Is Graph Bipartite?
# Concept: Graphs - BFS/DFS coloring, bipartite check.
# Approach:
#   - For each component, use BFS (or DFS) to try to color the graph with 2 colors.
#   - In BFS, use distance (level) to ensure no two adjacent nodes have the same parity.
#   - If any edge connects two nodes of the same color or level, the graph is not bipartite.
#   - Returns True if bipartite, False otherwise.
# Time Complexity: O(V + E), where V = number of vertices, E = number of edges.
# Space Complexity: O(V), for visited and distance arrays.

from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        adjList = graph

        visited = [-1 for _ in range(n)]
        distance = [-1 for _ in range(n)]
        color = [-1 for _ in range(n)]  # Used for optional DFS

        # BFS-based bipartite check (level coloring)
        def bfs(source):
            visited[source] = 1
            q = deque([source])
            distance[source] = 0
            while q:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.append(neighbor)
                        distance[neighbor] = 1 + distance[node]
                    else:
                        # If two neighbors are at the same level, odd-length cycle found
                        if distance[neighbor] == distance[node]:
                            return False
            return True

        # DFS-based bipartite check (explicit coloring)
        def dfs(node):
            visited[node] = 1
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    color[neighbor] = 1 if color[node] == 0 else 0
                    if not dfs(neighbor):
                        return False
                else:
                    if color[neighbor] == color[node]:
                        return False
            return True

        for v in range(n):
            if visited[v] == -1:
                color[v] = 0  # Only needed for DFS
                if not bfs(v):  # Swap to dfs(v) for the DFS approach
                    return False

        return True