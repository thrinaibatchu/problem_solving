# LeetCode Problem 200: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/description/
# Concept: Graphs. Traverse a 2D matrix using BFS to count connected components.
# Approach:
#   - Treat each '1' as a node and traverse using BFS to mark all land in the current island as visited.
#   - Increment the island count for each unvisited '1' found in the grid.
# Time Complexity: O(m * n), where m and n are grid dimensions.
# Space Complexity: O(min(m, n)) for the queue (worst-case island is the entire grid side).

from collections import deque
from typing import List  # Always nice to add for full type checking

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def getNeighbors(node):
            r, c = node
            neighbors = []
            if r > 0:
                neighbors.append((r-1, c))
            if c > 0:
                neighbors.append((r, c-1))
            if r < len(grid) - 1:
                neighbors.append((r+1, c))
            if c < len(grid[0]) - 1:
                neighbors.append((r, c+1))
            return neighbors

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'
            while q:
                node = q.popleft()
                neighbors = getNeighbors(node)
                for nr, nc in neighbors:
                    if grid[nr][nc] != '0':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))
        
        components = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != '0':
                    components += 1
                    bfs(r, c)

        return components
