# leetcode_733_flood_fill.py
# LeetCode Problem 733: Flood Fill
# Link: https://leetcode.com/problems/flood-fill/
# Name: Flood Fill
# Concept: Graphs - BFS/DFS traversal in a 2D grid (flood fill algorithm).
# Approach:
#   - Use BFS to traverse all connected pixels starting from (sr, sc) with the same original color.
#   - Change each connected pixel to the new color as you traverse.
#   - Early exit if the new color is the same as the starting color.
# Time Complexity: O(m * n), where m and n are the image dimensions.
# Space Complexity: O(m * n) in the worst case for the queue.

from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def getNeighbors(node):
            r, c = node
            neighbors = []
            if r > 0:
                neighbors.append((r-1, c))
            if c > 0:
                neighbors.append((r, c-1))
            if r < len(image) - 1:
                neighbors.append((r+1, c))
            if c < len(image[0]) - 1:
                neighbors.append((r, c+1))
            return neighbors
        
        def bfs(r, c):
            curr_color = image[r][c]
            if curr_color == color:
                return
            q = deque()
            q.append((r, c))
            image[r][c] = color
            while q:
                node = q.popleft()
                neighbors = getNeighbors(node)
                for nr, nc in neighbors:
                    if image[nr][nc] == curr_color:
                        q.append((nr, nc))
                        image[nr][nc] = color

        bfs(sr, sc)
        return image
