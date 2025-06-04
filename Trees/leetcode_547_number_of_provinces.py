# leetcode_547_number_of_provinces.py
# LeetCode Problem 547: Number of Provinces
# Link: https://leetcode.com/problems/number-of-provinces/
# Name: Number of Provinces (a.k.a. Zombie Clusters, Friend Circles)
# Concept: Graphs - DFS/BFS for connected components in adjacency matrix
# Approach:
#   - Each city is a node; isConnected[i][j] == 1 means a direct connection.
#   - Use DFS to visit all cities in the same province (cluster).
#   - Count the number of DFS calls from unvisited nodes = number of provinces.
# Time Complexity: O(N^2), N = number of cities.
# Space Complexity: O(N), for visited array and recursion stack.

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        n = len(isConnected)
        visited = [-1] * n

        def dfs(node):
            visited[node] = 1
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and visited[neighbor] == -1:
                    dfs(neighbor)

        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                dfs(v)

        return components
