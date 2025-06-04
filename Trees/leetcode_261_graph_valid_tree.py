# leetcode_261_graph_valid_tree.py
# LeetCode Problem 261: Graph Valid Tree
# Link: https://leetcode.com/problems/graph-valid-tree/
# Name: Graph Valid Tree
# Concept: Graphs, connected components, cycle detection (BFS/DFS)
# Approach:
#   - Check if the number of edges is exactly n-1 (a tree property).
#   - Build adjacency list for the undirected graph.
#   - Use DFS to detect cycles (with parent tracking).
#   - Ensure the graph is fully connected (only one component).
# Time Complexity: O(N + E), N = nodes, E = edges.
# Space Complexity: O(N + E), for adjacency list and visited arrays.

from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Build a graph
        adjList = [[] for _ in range(n)]
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = [-1 for _ in range(n)]
        parent = [-1 for _ in range(n)]

        def dfs(node):
            visited[node] = 1
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    parent[neighbor] = node
                    if dfs(neighbor):
                        return True  # Cycle found
                else:
                    if neighbor != parent[node]:
                        return True  # Cycle found
            return False

        connected = 0
        for v in range(n):
            if visited[v] == -1:
                connected += 1
                if connected > 1:
                    return False  # More than one component
                if dfs(v):
                    return False  # Cycle found
        return True
