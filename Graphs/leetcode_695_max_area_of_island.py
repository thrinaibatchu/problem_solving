# LeetCode Problem 695: Max Area of Island
# Link: https://leetcode.com/problems/max-area-of-island/
# Concept: Graphs. Traverse 2D grid using BFS to find the largest connected group of 1's (island).
# Approach:
#   - For every cell with value 1, start BFS and count the size of the connected island.
#   - Mark visited cells by setting them to 0 to avoid revisiting.
#   - Track and return the largest area found.
# Note: The input grid contains integers (0 for water, 1 for land).
# Time Complexity: O(m * n)
# Space Complexity: O(min(m, n))

from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getNeighbors(node):
            r, c = node
            neighbors = []
            if r > 0:
                neighbors.append((r-1, c))
            if c > 0:
                neighbors.append((r, c-1))
            if r < len(grid)-1:
                neighbors.append((r+1, c))
            if c < len(grid[0]) - 1:
                neighbors.append((r, c+1))
            return neighbors
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            count = 1
            while q:
                node = q.popleft()
                neighbors = getNeighbors(node)
                for nr, nc in neighbors:
                    if grid[nr][nc] != 0:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        count += 1
            return count

        max_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    max_count = max(max_count, bfs(r, c))
        return max_count
